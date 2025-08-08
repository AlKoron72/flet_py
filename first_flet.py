import flet as ft

class DataApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.items = []  # zentrale Datenhaltung
        self.list_view = ft.ListView(expand=True)
        self.input_field = ft.TextField(label="Neues Item")
        self.add_btn = ft.ElevatedButton("Hinzufügen", on_click=self.add_item)
        self.remove_btn = ft.ElevatedButton("Letztes entfernen", on_click=self.remove_item)

        self.layout = ft.Column(
            controls=[self.input_field, ft.Row([self.add_btn, self.remove_btn]), self.list_view],
            spacing=10
        )
        self.page.add(self.layout)

    def add_item(self, e):
        text = self.input_field.value.strip()
        if text:
            self.items.append(text)
            self.input_field.value = ""
            self.update_list()
            self.page.update()

    def remove_item(self, e):
        if self.items:
            self.items.pop()
            self.update_list()
            self.page.update()

    def update_list(self):
        # Liste neu aufbauen
        self.list_view.controls = [ft.Text(item) for item in self.items]

def main(page: ft.Page):
    page.title = "Datenhaltung in Klasse"
    DataApp(page)

if __name__ == "__main__":
    ft.app(target=main)
