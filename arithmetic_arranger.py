class TuclaseExamen():

    Problemas = []
    ViewResp = False

    def arithmetic_arranger(self, *args):
        opers = list()
        res = ''
        operaciones = args[0]
        print(operaciones)
        lineArriba = ''
        lineAbajo = ''
        lineSeparador = ''
        lineResult = ''

        if (len(operaciones) <= 5):
            for problem in operaciones:
                print(problem)
                if ("+" in problem) or ("-" in problem):

                    # print(problem)
                    prob = problem.split()
                    getNum1 = prob[0]
                    typeProblem = prob[1]
                    getNum2 = prob[2]
                    opers.append(typeProblem)

                    # Validar Numeros
                    if (getNum1.isdigit() and getNum2.isdigit()):
                        # Validar Longitud
                        
                        if len(getNum1.strip()) <= 4 and len(getNum2.strip()) <= 4:
                            # Validar Si Hay Más de 5 Problemas
                            digitos = max(len(getNum1), len(getNum2)) + 2
                            #print(digitos)

                            lineArriba += getNum1.rjust(digitos)
                            lineArriba += ' '*4

                            lineAbajo += typeProblem
                            lineAbajo += getNum2.rjust(digitos - 1)
                            lineAbajo += ' '*4

                            lineSeparador += '-' * digitos
                            lineSeparador += ' ' * 4

                            lineResult += str(eval(problem)).rjust(digitos)
                            lineResult += ' '*4
                        else:
                            return 'Error: Numbers cannot be more than four digits.'
                    else:
                        return 'Error: Numbers must only contain digits.'
                else:
                    return "Error: Operator must be '+' or '-'."
        else:
            return 'Error: Too many problems.'

        if args[1] :
            res = '\n'.join((lineArriba.rstrip(), lineAbajo.rstrip(), lineSeparador.rstrip(), lineResult.rstrip()))
        else:
            res = '\n'.join((lineArriba.rstrip(), lineAbajo.rstrip(), lineSeparador.rstrip()))

        return res
