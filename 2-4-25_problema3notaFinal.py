# Calcular nota final de un estudiante

varEstudiante = input("Ingrese su nombre: ")
varProgramacion = int(input("Nota obtenida en programacion basica: "))
varIngles1 = int(input("Nota obtenida en Ingles 1: "))
varTecnicasdecomunicacion = int(
    input("Nota obtenida en Tecnicas de computacion: "))
varFundamentoscompu = int(
    input("Nota obtenida en Fundamentos de comunicacion: "))
varNotafinal = (varProgramacion + varIngles1 +
                varFundamentoscompu + varTecnicasdecomunicacion) / 4

print("Hola", varEstudiante, "su nota final es", varNotafinal)
