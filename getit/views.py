from utils import load_data, load_template 

# Carrega e formata as anotações do JSON, unindo-as e retornando o HTML:
def index():
    # Carrega o template das notas:
    note_template = load_template('components/note.html')         
    
    # Monta a lista de anotações formatadas:
    notes_li = [
        note_template.format(title=dados['titulo'], details=dados['detalhes'])
        for dados in load_data('notes.json')
    ]                                                             
    
    # Une tudo em uma única string:
    notes = '\n'.join(notes_li)                                   

    # Retorna o HTML com as anotações:
    return load_template('index.html').format(notes=notes)        

# Adiciona a nova anotação ao arquivo JSON usando título e detalhes:
def submit(titulo, detalhes):
    # Importa a função para adicionar anotações:
    from utils import add_note                                    
    
    # Adiciona a nova anotação ao arquivo JSON:
    add_note(titulo, detalhes)                                    
