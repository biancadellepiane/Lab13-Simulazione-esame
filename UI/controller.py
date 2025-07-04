import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def filDDYear(self):
        years = self._model.getAllYear()
        for y in years:
            self._view._ddAnno.options.append(ft.dropdown.Option(y))
        self._view.update_page()

    def handleDDYearSelection(self, e):
        pass

    def handleCreaGrafo(self,e):
        year = self._view._ddAnno.value
        if year is None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Nessun valore inserito", color="red"))
            self._view.update_page()
            return

        self._model.buildGraph(year)

        numNodi, numArchi = self._model.graphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato:"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {numNodi}"))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {numArchi}"))

        bestPilota, punteggio = self._model.getMigliorPilota()
        self._view.txt_result.controls.append(ft.Text(f"Best driver: {bestPilota}, with Score: {punteggio} "))

        self._view.update_page()
    def handleCerca(self, e):
        pass