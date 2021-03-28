def form_save(form):
    if form.is_valid():
        return form.save()
    else:
        print(form)
        print(form.errors)
        return None


def forms_save(forms):
    for form in forms:
        if not form.is_valid():
            print(form.prefix)
            print(form.errors)
            return False
    for form in forms:
        print(f'Save - {form.prefix}')
        form.save()
    return True
