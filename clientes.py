
import csv, os, time
os.system('cls')
FECHA_EMI = 2

archivo_clientes  = "clientes.txt"
archivo_impuestos = "IMPUESTOS.csv"
tipo_doc = 80
DOCUMENTO_INDEX = 5
TIPO_COMPROBANTE_INDEX = 0
N_COMP_INDEX = 1
COD_LUGAR_EMISION = 1
IMP_GRAVADO_INDEX = 9
PORCENTAJE_ALICUOTA_INDEX = 8
IMPUESTO=10
tipFACA = 0
tipFACB = 0
tipNCA = 0
tipNCB = 0
tipDEBA = 0
tipDEBB = 0             

def main():
    
    file = read_file(archivo_impuestos)
    print(file)

def rellenar_ceros(numero):
    j="0"
    #length of the number
    length=len(numero)
    #aumento en 1 a length para cuadrar la cantidad de ceros a agregar
    ceros_faltantes = 15 - (length+1)
    #print(ceros_faltantes," ceros a agregar")
    while ceros_faltantes > 0:
        j="0"+j
        ceros_faltantes = ceros_faltantes-1
        #print("soy j + numero ",j+numero)
        #print("largo de j + numero es : ", len(j+numero))
        #time.sleep(6)
         
    return j+numero   #'''Ojo con el return, tiene q estar fuera del bucle'''

def my_float(num_fl):
    #antes
    print("antes ",type(num_fl))
    #funcion float conserva tal cual el nro
    flo_ = float(num_fl)
    print(type(flo_))
    print("my",flo_)
    return flo_

def read_file(file_name) :
    imp_gr=""
    with open(file_name, "rt") as filename_csv:
        os.system('cls')
        print("")
        print("*------------------------------------------------------------------------------------*")
        reader = csv.reader(filename_csv, delimiter=";")
        next(reader)
        for line in reader:
            #These lines parsed date
            fecha_emision = line[FECHA_EMI]
            date_ = fecha_emision.split('/')
            parsed_date = date_[2]+date_[1]+date_[0]
            docu = line[DOCUMENTO_INDEX]
            
            docu_splited = docu.split('-')
            d0 = docu_splited[0]
            d1 = docu_splited[1]
            d2 = docu_splited[2]
            documen=d0+d1+d2
            
            tipo_compr=line[TIPO_COMPROBANTE_INDEX]
            num_comp = line[N_COMP_INDEX]
            
            #numero de comprobante
            num_comp_parsed=num_comp[6:14]
            
            digit=num_comp[0:1]
            
            cod_lug_emi = line[COD_LUGAR_EMISION]
            parse_cod_lug_emi=cod_lug_emi[2:6]
            #impuesto gravado
            imp_grav = line[IMP_GRAVADO_INDEX]
            #Relleno con ceros hasta completar 15 digitos
            imp_gr = rellenar_ceros(imp_grav)
            porcent_alicuo=line[PORCENTAJE_ALICUOTA_INDEX]
            inpu=line[IMPUESTO]
            imp=rellenar_ceros(inpu)
            if tipo_compr =='FAC' and digit=='A':
                tipFACA = "01"
                with open("DATOS.TXT", "at") as d:
                    dt = f"{parsed_date}{tipo_doc}{documen}{tipFACA}{digit}{parse_cod_lug_emi}{num_comp_parsed}{imp}{porcent_alicuo}{imp_gr}"
                    #print(len(dt))
                    t = dt.strip()
                    print(t,file=d)
               
            elif tipo_compr =='FAC' and digit=='B':
                tipFACB = "06"
                #print("soy tipFACB",tipFACB)
               
                with open("DATOS.TXT", "at") as d:
                    dt = f"{parsed_date}{tipo_doc}{documen}{tipFACB}{digit}{parse_cod_lug_emi}{num_comp_parsed}{imp}{porcent_alicuo}{imp_gr}"
                    t= dt.strip()
                    print(t,file=d)
                 
            elif tipo_compr == 'N/C' and digit == 'A':
                 tipNCA = "03"
                 
                 #print("soy tipNCA",tipNCA)
                 
                 with open("DATOS.TXT", "at") as d:
                    dt = f"{parsed_date}{tipo_doc}{documen}{tipNCA}{digit}{parse_cod_lug_emi}{num_comp_parsed}{imp}{porcent_alicuo}{imp_gr}"
                    t= dt.strip()
                    print(t,file=d)
                 
            elif tipo_compr =='N/C' and digit == 'B':
                 tipNCB = "08"
                 #print("soy tipNCB",tipNCB)
                 
                 with open("DATOS.TXT", "at") as d:
                    dt = f"{parsed_date}{tipo_doc}{documen}{tipNCB}{digit}{parse_cod_lug_emi}{num_comp_parsed}{imp}{porcent_alicuo}{imp_gr}"
                    t= dt.strip()
                    print(t,file=d)
              
            elif tipo_compr =='DEB' and digit == 'A':
                 tipDEBA = "02"
                 #print("soy tipDEBA",tipDEBA)
                 
                 with open("DATOS.TXT", "at") as d:
                    dt = f"{parsed_date}{tipo_doc}{documen}{tipDEBA}{digit}{parse_cod_lug_emi}{num_comp_parsed}{imp}{porcent_alicuo}{imp_gr}"
                    t= dt.strip()
                    print(t,file=d)
                 
            elif tipo_compr =='DEB' and digit == 'B':
                 tipDEBB = "07" 
                 
                 with open("DATOS.TXT", "at") as d:
                    dt = f"{parsed_date}{tipo_doc}{documen}{tipDEBB}{digit}{parse_cod_lug_emi}{num_comp_parsed}{imp}{porcent_alicuo}{imp_gr}"
                    t= dt.strip()
                    print(t,file=d)
                 
            else:
                print("--- No EXISTE !!!-----")

if __name__== "__main__":
    main()        
