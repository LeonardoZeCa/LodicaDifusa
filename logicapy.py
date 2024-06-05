import tkinter as tk
from tkinter import messagebox

class SistemaExperto:
    def __init__(self):
        self.reglas = [
            {"sintomas": {"fiebre", "tos", "dolor_de_garganta"}, "diagnostico": "Gripe", "descripcion": "Infección viral común"},
            {"sintomas": {"fiebre", "tos", "dificultad_para_respirar"}, "diagnostico": "COVID-19", "descripcion": "Enfermedad respiratoria causada por el coronavirus"},
            {"sintomas": {"fiebre", "dolor_de_cabeza", "rigidez_en_el_cuello"}, "diagnostico": "Meningitis", "descripcion": "Infección de las membranas que rodean el cerebro y la médula espinal"},
            {"sintomas": {"dolor_de_garganta", "goteo_nasal", "estornudos"}, "diagnostico": "Resfriado Común", "descripcion": "Infección viral del tracto respiratorio superior"},
            {"sintomas": {"fiebre", "erupcion_cutanea", "dolor_en_las_articulaciones"}, "diagnostico": "Dengue", "descripcion": "Enfermedad viral transmitida por mosquitos"},
            {"sintomas": {"nauseas", "vomitos", "diarrea"}, "diagnostico": "Intoxicación Alimentaria", "descripcion": "Enfermedad causada por consumir alimentos contaminados"},
            {"sintomas": {"fatiga", "perdida_de_peso", "sed_excesiva"}, "diagnostico": "Diabetes", "descripcion": "Trastorno metabólico caracterizado por niveles elevados de azúcar en la sangre"},
            {"sintomas": {"dolor_abdominal", "fiebre", "malestar_general"}, "diagnostico": "Apendicitis", "descripcion": "Inflamación del apéndice"},
        ]
    
    def diagnosticar(self, sintomas):
        for regla in self.reglas:
            if regla["sintomas"].issubset(sintomas):
                return regla
        return {"diagnostico": "Diagnóstico no encontrado", "descripcion": ""}

class Aplicacion(tk.Tk):
    def __init__(self, sistema_experto):
        super().__init__()
        self.sistema_experto = sistema_experto
        self.title("Sistema Experto de Diagnóstico Médico")
        self.geometry("400x600")
        
        self.sintoma_vars = {
            "Fiebre": tk.BooleanVar(),
            "Tos": tk.BooleanVar(),
            "Dolor de Garganta": tk.BooleanVar(),
            "Dificultad para Respirar": tk.BooleanVar(),
            "Dolor de Cabeza": tk.BooleanVar(),
            "Rigidez en el Cuello": tk.BooleanVar(),
            "Goteo Nasal": tk.BooleanVar(),
            "Estornudos": tk.BooleanVar(),
            "Erupción Cutánea": tk.BooleanVar(),
            "Dolor en las Articulaciones": tk.BooleanVar(),
            "Náuseas": tk.BooleanVar(),
            "Vómitos": tk.BooleanVar(),
            "Diarrea": tk.BooleanVar(),
            "Fatiga": tk.BooleanVar(),
            "Pérdida de Peso": tk.BooleanVar(),
            "Sed Excesiva": tk.BooleanVar(),
            "Dolor Abdominal": tk.BooleanVar(),
            "Malestar General": tk.BooleanVar(),
        }
        
        self.crear_widgets()
    
    def crear_widgets(self):
        tk.Label(self, text="Seleccione sus síntomas:").pack(pady=10)
        
        for sintoma, var in self.sintoma_vars.items():
            tk.Checkbutton(self, text=sintoma, variable=var).pack(anchor='w')
        
        tk.Button(self, text="Diagnosticar", command=self.diagnosticar).pack(pady=20)
    
    def diagnosticar(self):
        sintomas = {sintoma.lower().replace(" ", "_") for sintoma, var in self.sintoma_vars.items() if var.get()}
        resultado = self.sistema_experto.diagnosticar(sintomas)
        messagebox.showinfo("Diagnóstico", f"Diagnóstico: {resultado['diagnostico']}\n\nDescripción: {resultado['descripcion']}")

if __name__ == "__main__":
    sistema_experto = SistemaExperto()
    app = Aplicacion(sistema_experto)
    app.mainloop()
