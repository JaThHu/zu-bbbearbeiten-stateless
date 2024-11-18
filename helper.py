from dataclasses import dataclass
import datetime

# Liste der To-dos
items = []

@dataclass
class Item:
    text: str
    date: datetime.date
    isCompleted: bool = False

def add(text, date):
    # Datum in datetime.date umwandeln
    parsed_date = datetime.datetime.strptime(date, '%Y-%m-%d').date()
    
    # Text anpassen und Item erstellen
    text = text.replace('b', 'bbb').replace('B', 'Bbb')
    new_item = Item(text=text, date=parsed_date)
    
    # Item zur Liste hinzufügen und sortieren
    items.append(new_item)
    items.sort(key=lambda x: x.date)

def get_all():
    return items

def get(index):
    return items[index]

def update(index):
    items[index].isCompleted = not items[index].isCompleted
