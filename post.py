# största delen av den h'r filen är skriven med chatgpt
# för jag kände verkligen inte för att programmera i
# python.


from datetime import datetime


datum_som_jag_skriver = input("Datum som (stil) jag skriver: ")


def convert_to_rfc822(date_str):
    try:
        # Omvandla strängen till ett datetime-objekt med formatet YYYY/MM/DD
        date_obj = datetime.strptime(date_str, "%Y/%m/%d")
        # Skapa en sträng med RFC 822-formatet
        rfc822_date = date_obj.strftime("%a, %d %b %Y %H:%M:%S +0000")
        return rfc822_date
    except ValueError:
        return "Ogiltigt datumformat. Använd formatet YYYY/MM/DD."

# Användaren anger datumet i formatet YYYY/MM/DD
input_date = input("Ange datumet (YYYY/MM/DD): ")
rfc822_date = convert_to_rfc822(input_date)
print("RFC 822-formatet: ", rfc822_date)



def get_text_between_lines(file_path, start_line):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        start_index = -1
        end_index = -1
        end_line = str(len(lines))

        for i, line in enumerate(lines):
            if start_line in line:
                start_index = i
            if end_line in line:
                end_index = i
                break

        if start_index == -1 or end_index == -1:
            return "Kunde inte hitta angivna linjer."

        # Hämta texten mellan de två linjerna (inklusive dessa linjer)
        text_between_lines = ''.join(lines[start_index:end_index + 1])

        return text_between_lines
    except IOError:
        return "Det uppstod ett fel vid läsning av filen."

# Anropa funktionen med sökväg till filen och de två linjerna du vill hämta texten mellan
file_path = "blogginlagg/raw/" + input("Ange filnamn (blogginlagg/raw/...):")
start_line = "4"
result_text = get_text_between_lines(file_path, start_line)
print(result_text)


def write_to_file(file_path, text, line_number):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Se till att line_number inte är utanför antalet rader i filen
        line_number = min(max(0, line_number - 1), len(lines))

        lines.insert(line_number, '\n' + text + '\n')

        with open(file_path, 'w') as file:
            file.writelines(lines)

        print(f"Texten har skrivits på rad {line_number + 1} i filen.")
    except IOError:
        print("Det uppstod ett fel vid skrivning till filen.")




# Anropa funktionen med sökväg till filen och textsträngen du vill skriva
file_path = "blogg.html"

text_to_write = """
<!DOCTYPE html>
<html>
<head>
  <title>""" + datum_som_jag_skriver + """</title>
  <style>
    body {
      font-family: "Consolas", monospace;
      font-size: 3vmin;
      width: 800px;
      margin: 0 auto;
      }
      .rainbow-divider {
      display: flex;
      height: 2px;
    }
  </style>
</head>
<body>

  <h1>Titel</h1>

  <b><p>""" + datum_som_jag_skriver + """<br><a href="../index.html">allanjoelwerner.com</a></p></b>
  <hr>

  """ + result_text + """

  <br><br><br>
</body>
</html>

"""

#write_to_file(file_path, text_to_write, 22)
print(text_to_write)



















