from document_system.complex_form import ComplexForm


class FormBuilder:
    def __init__(self) -> None:
        self.form_builder = ComplexForm()

    def reset(self) -> None:
        self.form_builder = ComplexForm()

    def get_form(self) -> ComplexForm:
        return self.form_builder

    def build_personal_section(self, heading: str) -> None:
        content = f"--{heading}--\n"
        content += "First name: < >\n"
        content += "Last name: < >\n"
        self.form_builder.extend_content(content)

    def build_details_section(self, details_heading: str) -> None:
        content = f"--{details_heading}--\n"
        content += "Age: < >\n"
        content += "Address: < >\n"
        self.form_builder.extend_content(content)

    def build_email_section(self) -> None:
        self.form_builder.extend_content('Email: <> \n')

    def build_phone_section(self) -> None:
        self.form_builder.extend_content('Nr.tel: <> \n')

    def build_ue_regulatory_info(self) -> None:
        self.form_builder.extend_content(f"UE info \n")

    def build_usa_regulatory_info(self) -> None:
        self.form_builder.extend_content(f"Some required in forms in USA \n")
