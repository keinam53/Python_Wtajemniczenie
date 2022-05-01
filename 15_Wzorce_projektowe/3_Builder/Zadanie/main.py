from document_system.form_builder import FormBuilder


def run() -> None:
    form = FormBuilder()
    form.build_personal_section('Personal info!')
    form.build_details_section('Personal details')
    form.build_email_section()
    form.build_ue_regulatory_info()
    personal_form_ue = form.get_form()
    print(personal_form_ue.render())

    print(20 * '-')

    form = FormBuilder()
    form.build_personal_section('Personal info!')
    form.build_details_section('Personal details')
    form.build_phone_section()
    form.build_usa_regulatory_info()
    personal_form_usa = form.get_form()
    print(personal_form_usa.render())


if __name__ == '__main__':
    run()
