function updateFormIndex(element, prefix, index) {
    let id_regex = new RegExp('(' + prefix + '-\\d+)');
	let replacement = prefix + '-' + index;
	let name = $(this).attr('name').replace(id_regex,replacement);
	let id = 'id_' + name;
    $(this).attr({'name': name, 'id': id}).val('');
}

function delForm(btn, prefix, form, counter) {
    $(btn).parents(form).remove();
    let forms = $(form);
    $('#id_' + prefix + '-TOTAL_FORMS').val(forms.length);

    for (var i=0, formCount=forms.length; i<formCount; i++) {
        element = $(forms.get(i));
        element.find(':input').each(function() {
            updateFormIndex(element, prefix, i)
        });
        if (counter) element.find(counter).text(i+1);
    }
    return false;
}

function addForm(prefix, form, counter, default_image_url) {
    let selector = form + ":last";
    let newElement = $(selector).clone(true);
    let total = $('#id_' + prefix + '-TOTAL_FORMS').val();
    let i = 0;
    newElement.find(':input').each(function() {
        let name = $(this).attr('name').replace('-' + (total-1) + '-','-' + total + '-');
        let id = 'id_' + name;
        $(this).attr({'name': name, 'id': id}).val('').removeAttr('checked');
    });
    newElement.find('.blocks-image').each(function() {
        $(this).css('background', 'url(' + default_image_url + ') no-repeat')
    });

    total++;
    $('#id_' + prefix + '-TOTAL_FORMS').val(total);
    if (counter) newElement.find(counter).each(function() { $(this).text(total); });
    $(selector).after(newElement);
}