# Workingtimepractice

### Erklärung der Bentzung
Dies ist ein Tool, das die Erfasssung der eigenen Arbeitszeit erleichtern soll. Man kann sich über die Branches zwischen zwei Versionen entscheiden. Die eine speichert die Daten nicht nur in einem Textdokument, sondern ist darüber hinaus noch mit einer Datenbank verknüpft.

#### Standardversion
Um die Standardversion zu benutzen, muss man lediglich das Python-Programm "main.py" auf seinem Rechner ausführen. Daraufhin fragt das Programm den Namen und die Uhrzeit des Arbeitsbeginn ab. Dauraufhin kann man selber entscheiden, ob und wie man weitermachen möchte. Man kann das Programm zwischendurch ohne Probleme beenden und später erneut öffnen, ohne dass die Daten dabei verloren gehen. Wichtig ist nur, dass man dies über den Befehl exit (e) tut, da nur dann die Daten gespeichert werden. Dies geschieht in einem Textdokument, das immer den Titel "workingtime_<Datum von heute>.txt" trägt und das man sich jederzeit angucken kann und in dem alle wichtigen Informationen zu finden sind. Später hat man dann für jeden Tag ein eigenes Textdokument und man kann genau sehen, wie lange man in der Vergangenheit gerabeitet hat. Wenn man am Ende des Tages alle Informationen eingetragen hat, kann man den Tag beenden. Dadurch wird die endgültige Arbeits- und Pausenzeit errechnet und gespeichert. Die Informationen kann man auch danach noch bearbeiten, man muss dann nur den Tag erneut beenden.

#### Datenbankversion
In der Datenbankversion kann man die Daten zusätzlcih zum Textdokument noch in einer Datenbank speichern. Dafür muss man nur die dafür vorgesehenen Felder im Quellcode mit den Datenbankinformationen ausfüllen. Ansonsten funktioniert das Programm genauso wie in der Standardversion. Man muss nur darauf achten, dass man seine Daten auch in die Datenbank hochlädt, wenn man dananch gefragt wird. Dies ist nur möglich, wenn man seinen Tag beendet hat. Man kann ganz einfach die Informationen in der Datenbank überschreiben. Dafür ist es nur wichtig, dass die Änderungen durch das Beenden des Tages speichert. 
Wichtig: Um die Datenbankversion benutzen zu können, muss man das dafür benötigte package installiert haben. Dafür navigiert man mit dem Windows Terminal in den Skript-Ordner von python und gibt den Befehl 

    python -m pip install mysql-connector-python

ein.
