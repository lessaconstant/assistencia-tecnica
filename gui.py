from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox
from cliente import Cliente
from tecnico import Tecnico
from ordemServico import OrdemServico
from especialidade import Especialidade
from log import Log

def BButton(master, text, command):
    style = ttk.Style()
    style.configure("RoundedButton.TButton", relief=RIDGE, background="#333", foreground="#333")
    button = ttk.Button(master, text=text, style="RoundedButton.TButton", command=command)
    return button

def MenuScreen():
    Menu = Tk()
    Menu.title("Assistencia Tecnica 9000")
    Menu.config(bg="#333", padx=100, pady=100)

    menuTitle = Label(Menu, text="Bem Vindo", fg="#F5F5F5", bg="#333")
    menuTitle.grid(row=0, column=1, pady=10, padx=10)

    menuButt = BButton(Menu, text="Cliente", command=ClientScreen)
    menuButt.grid(row=2, column=1, padx=10, pady=10)

    menuButt = BButton(Menu, text="Tecnico", command=TecnicoScreen)
    menuButt.grid(row=3, column=1, padx=10, pady=10)

    menuButt = BButton(Menu, text="Ordem de Serviço", command=Os2)
    menuButt.grid(row=4, column=1, padx=10, pady=10)
    Menu.mainloop()

def ClientScreen():

    ClienteScreen = tk.Toplevel()
    ClienteScreen.title("AT9000 Clientes")
    ClienteScreen.config(bg="#333", padx=50, pady=50)

    clienButt = BButton(ClienteScreen, text="Adicionar Cliente", command=AddClientScreen)
    clienButt.grid(row=0, column=0, padx=15, pady=20)

    clienButt = BButton(ClienteScreen, text="Atualizar Cliente", command=selectClienteScreen)
    clienButt.grid(row=0, column=1, padx=15, pady=20)

def AddClientScreen():

    def storeClientInMemory():
####### place try except here
        name = nameEntry.get()
        cpf = cpfEntry.get()
        phone = phoneEntry.get()
        client = Cliente(name, cpf, phone)
        Cliente.listaCliente.append(client)
        Cliente.addSingleCliente(client)
        messagebox.showinfo('Dados Salvos', 'Cliente adicionado com sucesso!')
        AddClientScreen.destroy()
        

    AddClientScreen = tk.Toplevel()
    AddClientScreen.title("AT9000 Adicionar Cliente")
    AddClientScreen.config(bg="#333", padx=50, pady=50)

    clienText = Label(AddClientScreen, text="Nome", fg="#F5F5F5", bg="#333")
    clienText.grid(row=0, column=0, padx=10, pady=2)

    clienText = Label(AddClientScreen, text="CPF", fg="#F5F5F5", bg="#333")
    clienText.grid(row=1, column=0, padx=10, pady=2)

    clienText = Label(AddClientScreen, text="Telefone", fg="#F5F5F5", bg="#333")
    clienText.grid(row=2, column=0, padx=10, pady=2)

    nameEntry = Entry(AddClientScreen, width=20)
    nameEntry.grid(row=0, column=1)

    cpfEntry = Entry(AddClientScreen, width=20)
    cpfEntry.grid(row=1, column=1)
    
    phoneEntry = Entry(AddClientScreen, width=20)
    phoneEntry.grid(row=2, column=1)

    clienButt = BButton(AddClientScreen, text="Adicionar Cliente", command=storeClientInMemory)
    clienButt.grid(row=3, column=0, columnspan=2, padx=15, pady=20)
        
def updateClientScreen(index):

    def updateClientInMemory():
####### place try except here
        name = nameEntry.get()
        cpf = cpfEntry.get()
        phone = phoneEntry.get()
        client = Cliente(name, cpf, phone)

        for x in Cliente.listaCliente:
            if x.cpf == cpf:
                Cliente.listaCliente.remove(x)
        Cliente.delDataBase(cpf)

        Cliente.listaCliente.append(client)
        Cliente.addSingleCliente(client)

        messagebox.showinfo('Dados Salvos', 'Cliente atualizado com sucesso!')
        clientToUpdateScreen.destroy()
        
    clientToUpdate = Cliente.listaCliente[index]

    clientToUpdateScreen = tk.Toplevel()
    clientToUpdateScreen.title("AT9000 Atualizar Cliente")
    clientToUpdateScreen.config(bg="#333", padx=50, pady=50)

    clienText = Label(clientToUpdateScreen, text="Nome", fg="#F5F5F5", bg="#333")
    clienText.grid(row=0, column=0, padx=10, pady=2)

    clienText = Label(clientToUpdateScreen, text="CPF", fg="#F5F5F5", bg="#333")
    clienText.grid(row=1, column=0, padx=10, pady=2)

    clienText = Label(clientToUpdateScreen, text="Telefone", fg="#F5F5F5", bg="#333")
    clienText.grid(row=2, column=0, padx=10, pady=2)

    nameEntry = Entry(clientToUpdateScreen, width=20)
    nameEntry.grid(row=0, column=1)
    nameEntry.insert(0, clientToUpdate.nome)
    
    cpfEntry = Entry(clientToUpdateScreen, width=20)
    cpfEntry.grid(row=1, column=1)
    cpfEntry.insert(0, clientToUpdate.cpf)
    cpfEntry.config(state= "disabled")
    
    phoneEntry = Entry(clientToUpdateScreen, width=20)
    phoneEntry.grid(row=2, column=1)
    phoneEntry.insert(0, clientToUpdate.telefone)

    clienButt = BButton(clientToUpdateScreen, text="Atualizar Cliente", command=updateClientInMemory)
    clienButt.grid(row=3, column=0, columnspan=2, padx=15, pady=20)

def selectClienteScreen():

    def openUpdateClientScreen():
      indexTuple = clientesListbox.curselection()
      if len(indexTuple) != 0:
        index = indexTuple[0]
        updateClientScreen(index)
    
    def updateList():
        clientesListbox.delete(0, END)
        for cliente in Cliente.listaCliente:
            clientesListbox.insert(tk.END, cliente.nome)
        clientesListbox.grid(row=0, column=0, padx=10, pady=10)

    AtuClientScreen = tk.Toplevel()
    AtuClientScreen.title("AT9000 Atualizar Clientes")
    AtuClientScreen.config(bg="#333", padx=50, pady=50)

    clientesListbox = Listbox(AtuClientScreen, width=40)
    updateList()    

    AtuButt = BButton(AtuClientScreen, text="Atualizar Lista Cliente", command=updateList)
    AtuButt.grid(row=1, column=0, padx=10, pady=5)

    AtuButt = BButton(AtuClientScreen, text="Atualizar Cliente", command=openUpdateClientScreen)
    AtuButt.grid(row=1, column=1, padx=10, pady=5)

def Os2():
    Os2Screen = tk.Toplevel()
    Os2Screen.title("AT9000 OS")
    Os2Screen.config(bg="#333", padx=50, pady=50)

    Os2Butt1 = BButton(Os2Screen, text="Nova Ordem de Serviço", command=NovaOSScreen)
    Os2Butt1.grid(row=1, column=1, pady=5)

    Os2Butt2 = BButton(Os2Screen, text="Abrir Ordem de Serviço", command=selectOS)
    Os2Butt2.grid(row=2, column=1, pady=5)

def NovaOSScreen():
    NOsScreen = tk.Toplevel()
    NOsScreen.title("AT9000 Nova OS")
    NOsScreen.config(bg="#333", padx=50, pady=50)

    NOsLabel = Label(NOsScreen, text="Selecionar Cliente", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=0, column=0, padx=10, pady=(2, 10))

    NOsCombobox = ttk.Combobox(NOsScreen)
    NOsCombobox['values'] = ["".join(x.cpf+" - "+x.nome) for x in Cliente.listaCliente]
    NOsCombobox.grid(row=1, column=0, padx=20, pady=2)

    NOsLabel = Label(NOsScreen, text="Selecionar Técnico", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=2, column=0, padx=10, pady=2)

    NOsCombobox = ttk.Combobox(NOsScreen)
    NOsCombobox['values'] = [tecnico.nome for tecnico in Tecnico.listaTecnico]
    NOsCombobox.grid(row=3, column=0, padx=20, pady=2)

    NOsLabel = Label(NOsScreen, text="Descrição", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=0, column=1, padx=10, pady=(2, 10))

    issueDescriptionEntry = Text(NOsScreen, height=10, width=30)
    issueDescriptionEntry.grid(row=1, column=1, padx=10, pady=2, rowspan=5)

    NOsLabel = Label(NOsScreen, text="Equipamento(s)", fg="#F5F5F5", bg="#333")
    NOsLabel.grid(row=6, column=0, padx=10, pady=2)
    equipamentDescriptionEntry = Text(NOsScreen, height=10, width=30)
    equipamentDescriptionEntry.grid(row=7, column=0, padx=10, pady=2, rowspan=5)

    NOsButton = BButton(NOsScreen, text="Salvar", command=None)
    NOsButton.grid(row=6, column=1, padx=10, pady=2)

def TecnicoScreen(): 
    TecnicoScreen = tk.Toplevel()
    TecnicoScreen.title("AT9000 Tecnicos")
    TecnicoScreen.config(bg="#333", padx=50, pady=50)

    TecButt = BButton(TecnicoScreen, text="Adicionar Tecnico", command=AddTecnicoScreen)
    TecButt.grid(row=0, column=0, padx=15, pady=20)

    TecButt = BButton(TecnicoScreen, text="Atualizar Tecnico", command=selectTecnicoScreen)
    TecButt.grid(row=0, column=1, padx=15, pady=20)

def AddTecnicoScreen():

    def storetTecInMemory():
####### place try except here
        nome = TecNomeEntry.get()
        matricula = TecCpfEntry.get()
        especialidade = TecEspecialidadeCombobox.get()
        tec = Tecnico(nome, matricula, especialidade)
        Tecnico.listaTecnico.append(tec)
        Tecnico.addDataBaseTec(Tecnico.listaTecnico)
        messagebox.showinfo('Dados Salvos', 'Técnico adicionado com sucesso!')
        addTecnicoScreen.destroy()

    addTecnicoScreen = tk.Toplevel()
    addTecnicoScreen.title("AT9000 Adicionar Tecnicos")
    addTecnicoScreen.config(bg="#333", padx=50, pady=50)

    LabelTecNome = Label(addTecnicoScreen, text="Nome", fg="#F5F5F5", bg="#333")
    LabelTecNome.grid(row=0, column=1, padx=10, pady=2)
    TecNomeEntry = Entry(addTecnicoScreen, width=20)
    TecNomeEntry.grid(row=0, column=2)
    
    LabelTecMatricula = Label(addTecnicoScreen, text="Matricula", fg="#F5F5F5", bg="#333")
    LabelTecMatricula.grid(row=1, column=1, padx=10, pady=2)
    TecCpfEntry = Entry(addTecnicoScreen, width=20)
    TecCpfEntry.grid(row=1, column=2)

    LabelTecEspecialidade = Label(addTecnicoScreen, text="Especialidade", fg="#F5F5F5", bg="#333")
    LabelTecEspecialidade.grid(row=2, column=1, padx=10, pady=2)
    TecEspecialidadeCombobox = ttk.Combobox(addTecnicoScreen)
    TecEspecialidadeCombobox['values'] = [especialidade.name for especialidade in Especialidade]
    TecEspecialidadeCombobox.grid(row=2, column=2, padx=17, pady=2)
    
    TecButt = BButton(addTecnicoScreen, text="Adicionar Tecnico", command=storetTecInMemory)
    TecButt.grid(row=3, column=2, padx=7, pady=20)

def selectTecnicoScreen():

    def updateList():
        TecListbox.delete(0, END)
        for tec in Tecnico.listaTecnico:
            TecListbox.insert(tk.END, tec.nome)
    
    def openUpdateClientScreen():
        indexTuple = TecListbox.curselection()
        if len(indexTuple) != 0:
            index = indexTuple[0]
            updateTecnicoScreen(index)
    
    TecnicoScreen = tk.Toplevel()
    TecnicoScreen.title("AT9000 Atualizar Tecnico")
    TecnicoScreen.config(bg="#333", padx=50, pady=50)

    TecListbox = Listbox(TecnicoScreen, width=40)
    TecListbox.grid(row=0, column=0, padx=10, pady=10)
    updateList()

    TecButt = BButton(TecnicoScreen, text="Atualizar Lista", command=updateList)
    TecButt.grid(row=1, column=0, padx=10, pady=5)

    TecButt = BButton(TecnicoScreen, text="Atualizar Tecnico", command=openUpdateClientScreen)
    TecButt.grid(row=1, column=1, padx=10, pady=5)

def updateTecnicoScreen(index):

    def updateTecInMemory():
####### place try except here
        nome = TecNomeEntry.get()
        matricula = TecMatriculaEntry.get()
        especialidade = TecEspecialidadeCombobox.get()
        tec = Tecnico(nome, matricula, especialidade)
        for x in Tecnico.listaTecnico:
            if x.matricula == matricula:
                Tecnico.listaTecnico.remove(x)

        Tecnico.delDataBase(matricula)
        Tecnico.listaTecnico.append(tec)
        Tecnico.addDataBaseTec(Tecnico.listaTecnico)
        messagebox.showinfo('Dados Salvos', 'Técnico atualizado com sucesso!')
        updateTecnicoScreen.destroy()     

    tecToUpdate = Tecnico.listaTecnico[index]

    addTecnicoScreen = tk.Toplevel()
    addTecnicoScreen.title("AT9000 Adicionar Tecnicos")
    addTecnicoScreen.config(bg="#333", padx=50, pady=50)

    LabelTecNome = Label(addTecnicoScreen, text="Nome", fg="#F5F5F5", bg="#333")
    LabelTecNome.grid(row=0, column=1, padx=10, pady=2)
    TecNomeEntry = Entry(addTecnicoScreen, width=20)
    TecNomeEntry.grid(row=0, column=2)
    TecNomeEntry.insert(0, tecToUpdate.nome)
    
    LabelTecMatricula = Label(addTecnicoScreen, text="Matricula", fg="#F5F5F5", bg="#333")
    LabelTecMatricula.grid(row=1, column=1, padx=10, pady=2)
    TecMatriculaEntry = Entry(addTecnicoScreen, width=20)
    TecMatriculaEntry.grid(row=1, column=2)
    TecMatriculaEntry.insert(0, tecToUpdate.matricula)

    LabelTecEspecialidade = Label(addTecnicoScreen, text="Especialidade", fg="#F5F5F5", bg="#333")
    LabelTecEspecialidade.grid(row=2, column=1, padx=10, pady=2)
    TecEspecialidadeCombobox = ttk.Combobox(addTecnicoScreen)
    TecEspecialidadeCombobox['values'] = [especialidade.name for especialidade in Especialidade]
    TecEspecialidadeCombobox.grid(row=2, column=2, padx=17, pady=2)
    TecEspecialidadeCombobox.current(int(Especialidade[tecToUpdate.especialidade].value))
    
    TecButt = BButton(addTecnicoScreen, text="Adicionar Tecnico", command=updateTecInMemory)
    TecButt.grid(row=3, column=2, padx=7, pady=20)

def selectOS():
    def searchByCpf():
        cpf = searchBar.get()
        OSListbox.delete(0, END)
        for os in OrdemServico.listaOS:
            if os.client == cpf:
                OSListbox.insert(tk.END, "".join("#"+os.id+" "+os.status+" - "+os.equipamento))
    
    def openViewOS():
        osId = OSListbox.get(ANCHOR)
        if osId:
            osId = osId[1:7]
            selectedOs = [os for os in OrdemServico.listaOS if os.id == osId]
            if len(selectedOs)==0:
                print("Error")
            else:
                os = selectedOs[0]
            ViewOS(os)
        else:
            messagebox.showinfo('Error', 'Nenhuma OS selecionada')
    
    selectOS = tk.Toplevel()
    selectOS.title("AT9000 Selecionar Ordem de Serviço")
    selectOS.config(bg="#333", padx=50, pady=50)

    searchBar = tk.Entry(selectOS, width=20)
    searchBar.grid(row=0, column=1)

    OSListbox = Listbox(selectOS, width=40)
    OSListbox.grid(row=1, column=0, padx=10, pady=10)
    
    osSearchButton = BButton(selectOS, text="Pesquisar OS por CPF", command=searchByCpf)
    osSearchButton.grid(row=1, column=1, padx=10, pady=5)
    osOpenButton = BButton(selectOS, text="Abrir OS Selecionada", command=openViewOS)
    osOpenButton.grid(row=2, column=1, padx=10, pady=5)

def ViewOS(selectedOs):
    def NewComentScreen():
        NewComentScreen = tk.Toplevel()
        NewComentScreen.title("AT9000 Novo Comentario")
        NewComentScreen.config(bg="#333", padx=25, pady=25)

        NCLabel = Label(NewComentScreen, text="Comentário", fg="#F5F5F5", bg="#333")
        NCLabel.grid(row=0, column=0, padx=10, pady=2, sticky=N)

        NCEntry = Text(NewComentScreen, height=10 ,width=30)
        NCEntry.grid(row=0, column=1, padx=10, pady=2, sticky=S)

        NCButton = BButton(NewComentScreen, text=("Adicionar Comentário"), command=None)
        NCButton.grid(row=1, column=1, padx=10, pady=2, sticky=W)

        # def timestamp(self):
        # savedTime = time.localtime(self.__timestamp)
        # time_string = time.strftime("%d/%m/%Y, %H:%M:%S", savedTime)
        # return time_string

    def AttScreen():
        AttScreen = tk.Toplevel()
        AttScreen.title("AT9000 Atualizar Status")
        AttScreen.config(bg="#333", padx=25, pady=25)

        StatusLabel = Label(AttScreen, text="Status", fg="#F5F5F5", bg="#333")
        StatusLabel.grid(row=0, column=0, padx=10, pady=2)

        StatusComboBox = ttk.Combobox(AttScreen)
        # Joia
        StatusComboBox.grid(row=0, column=1, padx=10, pady=2)

        StatusButton = BButton(AttScreen, text="Atualizar", command=None)
        StatusButton.grid(row=1, column=1, padx=10, pady=2)
    
    ViewOSScreen = Tk()
    ViewOSScreen.title("AT9000 Visualizar OS")
    ViewOSScreen.config(bg="#333", padx=50, pady=50)
    
    CodigoLabel = Label(ViewOSScreen, text="Código :", fg="#F5F5F5", bg="#333")
    CodigoText = Label(ViewOSScreen, text=selectedOs.id, fg="#F5F5F5", bg="#333")
    CodigoLabel.grid(row=0, column=0, padx=10, pady=2, sticky=W)
    CodigoText.grid(row=0, column=1, padx=10, pady=2, sticky=W)

    TecnicoLabel = Label(ViewOSScreen, text="Técnico :", fg="#F5F5F5", bg="#333")
    TecnicoText = Label(ViewOSScreen, text=[tec.nome for tec in Tecnico.listaTecnico if tec.matricula == selectedOs.tecnico][0], fg="#F5F5F5", bg="#333")
    TecnicoLabel.grid(row=0, column=3, padx=10, pady=2, sticky=E)
    TecnicoText.grid(row=0, column=4, padx=10, pady=2, sticky=W)

    ClienteLabel = Label(ViewOSScreen, text="Cliente :", fg="#F5F5F5", bg="#333")
    ClienteText = Label(ViewOSScreen, text=[cliente.nome for cliente in Cliente.listaCliente if cliente.cpf == selectedOs.client][0], fg="#F5F5F5", bg="#333")
    ClienteLabel.grid(row=1, column=0, padx=10, pady=2, sticky=W)
    ClienteText.grid(row=1, column=1, padx=10, pady=2, sticky=W)

    StatusLabel = Label(ViewOSScreen, text="Status :", fg="#F5F5F5", bg="#333")
    StatusText = Label(ViewOSScreen, text=selectedOs.status, fg="#F5F5F5", bg="#333")
    StatusLabel.grid(row=1, column=3, padx=10, pady=2, sticky=E)
    StatusText.grid(row=1, column=4, padx=10, pady=2, sticky=W)

    Divisiao = Label(ViewOSScreen, text="     ", fg="#F5F5F5", bg="#333")
    Divisiao.grid(row=2, column=3, padx=10, pady=10)

    EquipamentoLabel = Label(ViewOSScreen, text="Equipamento :", fg="#F5F5F5", bg="#333")
    EquipamentoText = Label(ViewOSScreen, text=selectedOs.equipamento, fg="#F5F5F5", bg="#333")
    EquipamentoLabel.grid(row=3, column=0, padx=10, pady=2, sticky=W)
    EquipamentoText.grid(row=3, column=1, padx=10, pady=2, sticky=W)    
    
    descricaoLabel = Label(ViewOSScreen, text="Descrição do Problema :", fg="#F5F5F5", bg="#333")
    descricaoLabel.grid(row=3, column=0, padx=10, pady=2, sticky=W)
    
    descricaoText = Label(ViewOSScreen, text=selectedOs.descricao, fg="#F5F5F5", bg="#333")
    descricaoText.grid(row=3, column=1, padx=10, pady=2, sticky=W)

    ComentariosLabel = Label(ViewOSScreen, text="Comentários :", fg="#F5F5F5", bg="#333")
    ComentariosLabel.grid(row=4, column=0, padx=10, pady=2, sticky=W)
    
    comentarios = [log for log in Log.listaDeLogs if log.idOS == selectedOs.id]
    scrollbar = tk.Scrollbar(orient="horizontal")
    ComentariosText = Text(ViewOSScreen, fg="#F5F5F5", bg="#333", xscrollcommand=scrollbar.set)
    ComentariosText.grid(row=5, column=1, padx=10, pady=2, sticky=W)
    for comentario in comentarios:
        ComentariosText.insert(END, str(comentario) + "\n")
    ComentariosText.config(state=DISABLED)

    NewComentButton = BButton(ViewOSScreen, text=("Adicionar Comentário"), command=NewComentScreen)
    NewComentButton.grid(row=6, column=1, padx=10, pady=2, sticky=W)

    AttButton = BButton(ViewOSScreen, text=("Atualizar Status"), command=AttScreen)
    AttButton.grid(row=6, column=1, padx=10, pady=2, sticky=E)

if __name__ == "__main__":
    MenuScreen()
