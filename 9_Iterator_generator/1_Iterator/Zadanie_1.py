from __future__ import annotations


class PhoneApps:
    def __init__(self) -> None:
        self.system_app: list[str] = []
        self.user_app: list[str] = []

    def install_system_app(self, app: str) -> None:
        self.system_app.append(app)

    def install_user_app(self, app: str) -> None:
        self.user_app.append(app)

    def __iter__(self) -> AppsIterator:
        return AppsIterator(self.system_app, self.user_app)


class AppsIterator:
    def __init__(self, system_app: list[str], user_app: list[str]):
        self.system_app = system_app
        self.user_app = user_app
        self.system_app_index = 0
        self.user_app_index = 0

    def __int__(self) -> AppsIterator:
        return self

    def __next__(self) -> str:
        while self.system_app_index < len(self.system_app):
            element_to_return = self.system_app[self.system_app_index]
            self.system_app_index += 1
            return element_to_return

        while self.user_app_index < len(self.user_app):
            element_to_return = self.user_app[self.user_app_index]
            self.user_app_index += 1
            return element_to_return

        raise StopIteration


def run() -> None:
    my_apps = PhoneApps()
    my_apps.install_user_app("Facebook")
    my_apps.install_system_app("Sklep Play")
    my_apps.install_user_app("Spotify")

    for app in my_apps:
        print(app)


if __name__ == "__main__":
    run()

