import csv


"""
Coder: Shahaed Hasan
Date Started: June29
#
Description: Will hopefully read SDS and output relevant data into a CSV
"""



def SectionSplit(filename):
    """Function that takes a utf-8 text file name (specifically data sheets from sciencelab.com)
     and separates according to sections. Will return 16 different lists corresponding to each section
     #
     TODO: The control flow is NOT ERROR PROOF. Will break when one section is not found. In addition
     probably not very efficient & redundant. Also need to go ± 1~2 lines of each section because the pdf2txt
     at the end of pdf pages isnt great
     """

    lines = open(filename, encoding='utf-8').read().splitlines()

    Section0 = []
    Section1 = []
    Section2 = []
    Section3 = []
    Section4 = []
    Section5 = []
    Section6 = []
    Section7 = []
    Section8 = []
    Section9 = []
    Section10 = []
    Section11 = []
    Section12 = []
    Section13 = []
    Section14 = []
    Section15 = []
    Section16 = []

    # Search and split by sections
    i = 0
    while i != len(lines):

        if lines[i] == 'Section 1: Chemical Product and Company Identification':
            section0 = lines[0:i-1]
            section1index=i
            i += 1


        if lines[i] == 'Section 2: Composition and Information on Ingredients':
            section1 = lines[section1index:i-1]
            section2index = i
            i += 1

        if lines[i] == 'Section 3: Hazards Identification':
            section2 = lines[section2index:i-1]
            section3index = i
            i += 1

        if lines[i] == "Section 4: First Aid Measures":
            section3 = lines[section3index:i-1]
            section4index = i
            i += 1

        if lines[i] == 'Section 5: Fire and Explosion Data':
            section4 = lines[section4index:i-1]
            section5index = i
            i += 1

        if lines[i] == 'Section 6: Accidental Release Measures':
            section5 = lines[section5index:i-1]
            section6index = i
            i += 1

        if lines[i] == 'Section 7: Handling and Storage':
            section6 = lines[section6index:i-1]
            section7index = i
            i += 1

        if lines[i] == 'Section 8: Exposure Controls/Personal Protection':
            section7 = lines[section7index:i-1]
            section8index = i
            i += 1

        if lines[i] == 'Section 9: Physical and Chemical Properties':
            section8 = lines[section8index:i-1]
            section9index = i
            i += 1

        if lines[i] == 'Section 10: Stability and Reactivity Data':
            section9 = lines[section9index:i-1]
            section10index = i
            i += 1

        if lines[i] == 'Section 11: Toxicological Information':
            section10 = lines[section10index:i-1]
            section11index = i
            i += 1

        if lines[i] == 'Section 12: Ecological Information':
            section11 = lines[section11index:i-1]
            section12index = i
            i += 1

        if lines[i] == 'Section 13: Disposal Considerations':
            section12 = lines[section12index:i-1]
            section13index = i
            i += 1

        if lines[i] == 'Section 14: Transport Information':
            section13 = lines[section13index:i-1]
            section14index = i
            i += 1

        if lines[i] == 'Section 15: Other Regulatory Information':
            section14 = lines[section14index:i-1]
            section15index = i
            i += 1

        if lines[i] == 'Section 16: Other Information':
            section15 = lines[section15index:i-1]
            section16index = i
            section16 = lines[i:-1]
            i += 1

        else:
            i += 1


    SDS = {'Section0': section0, 'Section1': section1, 'Section2': section2, 'Section3' : section3, 'Section4' : section4,
           'Section5': section5, 'Section6': section6, 'Section7': section7, 'Section8': section8, 'Section9': section9,
           'Section10': section10, 'Section11': section11, 'Section12': section12, 'Section13' : section13,
           'Section14' : section14,'Section15': section15, 'Section16': section16}

    return SDS

def Section9Parse(Section9):
    """This shall parse the chemical data. Turn Up"""

    #Declare Variables as "Not available" if they are not found in the data sheet

    odor = taste = physical_state = color = boil_point = melt_point = crit_temp = vapor_pressure = "N/A"
    vapor_density = volatility = water_oil = ionicity = solubility = dispersion = MW = pH = "N/A"


    #Loop that looks for odor, taste, etc. Then splits them by the colon and put the second element in the variable.
    #If the second element is empty, look at the next item in the list. Happens in solubility & other long descriptions.
    #It usually means the splitter put it into another element of the list.
    for index, entry in enumerate(Section9):

        if entry.find("Odor:") != -1:
            odor = entry.split(":")[1]
        elif entry.find("Taste") != -1:
            taste = entry.split(":")[1]
        elif entry.find("Physical state and appearance") != -1:
            physical_state = entry.split(":")[1]
        elif entry.find("Molecular Weight") != -1:
            MW = entry.split(":")[1]
        elif entry.find("Color") != -1:
            color = entry.split(":")[1]
        elif entry.find("pH") != -1:
            pH = entry.split(":")[1]
        elif entry.find("Boiling Point") != -1:
            boil_point = entry.split(":")[1]
        elif entry.find("Melting Point") != -1:
            melt_point = entry.split(":")[1]
        elif entry.find("Critical Temperature") != -1:
            crit_temp = entry.split(":")[1]
        elif entry.find("Vapor Pressure") != -1:
            vapor_pressure = entry.split(":")[1]
        elif entry.find("Vapor Density") != -1:
            vapor_density = entry.split(":")[1]
        elif entry.find("Volatility") != -1:
            volatility = entry.split(":")[1]
        elif entry.find("Water/Oil") != -1:
            water_oil = entry.split(":")[1]
        elif entry.find("Ionicity") != -1:
            ionicity = entry.split(":")[1]
        elif entry.find("Dispersion") != -1:
            if entry.split(":")[1]:
                dispersion = entry.split(":")[1]
            else:
                dispersion = Section9[index + 1]
        elif entry.find("Solubility") != -1:
            if entry.split(":")[1]:
                solubility = entry.split(":")[1]
            else:
                solubility = Section9[index + 1]

    properties = {"Odor" : odor, 'Taste' : taste, 'Physical State' : physical_state,
                    'Color' :  color, 'Boiling Point' : boil_point, 'Melting Point' : melt_point,
                'Critical Temperature': crit_temp, 'Vapor pressure' : vapor_pressure, 'Molecular Weight' : MW,
                  "Vapor Density" : vapor_density, 'Volatility' : volatility, 'Water/Oil Coeff' : water_oil,
                "Ionicity" : ionicity, 'Solubility' : solubility, 'Dispersion' : dispersion, 'pH' : pH,}

    return properties

def Section1Parse(Section1):
    """Will go through section 1 and parse 4 pieces of info name, cas, chem name, and chem formula. Returns a dict with
    keys that equate to the 4 things"""
    name = cas = chem_name = chem_formula = "N/A"

    for index, entry in enumerate(Section1):

        if entry.find("Product Name:") != -1:
            name = entry.split(":")[1]
        elif entry.find("CAS#:") != -1:
            cas = entry.split(":")[1]
        elif entry.find("Chemical Name:") != -1:
            chem_name = entry.split(":")[1]
        elif entry.find("Chemical Formula:") != -1:
            chem_formula = entry.split(":")[1]

    info = {"Name": name, "CAS#": cas, "Chemical Name": chem_name, "Chemical Formula": chem_formula}
    return info

def writeCSV(data, filename):
    """Will Write Data into a CSV
        Takes in data of format: [ {info},{}, ... ]
        and a file name to write to.

        TODO: Add more headers and other section data
    """

    #filename = filename + ".csv"

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ('Odor', 'Taste', 'Physical State', 'Color', 'Boiling Point', 'Melting Point',
                      'Critical Temperature', 'Vapor pressure', 'Molecular Weight', "Vapor Density",
                      'Volatility', 'Water/Oil Coeff', "Ionicity", 'Solubility', 'Dispersion', 'pH')
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
        headers = dict((n, n) for n in fieldnames)
        writer.writerow(headers)
        for chem in data:
            writer.writerow(chem)
    return


def main():

    sds1 = Section9Parse(SectionSplit("dca.txt")["Section9"])
    sds2 = Section9Parse(SectionSplit("ATC.txt")["Section9"])


    print(SectionSplit("dca.txt")["Section1"])
    print(SectionSplit("ATC.txt")["Section1"])
    writeCSV([sds1,sds2], "test.csv")


if __name__ == "__main__":
    main()
