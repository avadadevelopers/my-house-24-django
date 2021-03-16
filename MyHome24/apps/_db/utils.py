def form_save(form, alerts, alert_text):
    if form.is_valid():
        form.save()
        alerts.append(alert_text)