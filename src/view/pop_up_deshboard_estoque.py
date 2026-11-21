import customtkinter as ctk


class PopUpNovoItem(ctk.CTkToplevel):
    # "pai" é o DashboardEstoque (a janela que já está aberta)
    # é dele que o pop-up pega as cores e as funções de criar widgets (criar_entry, criar_botao...)
    def __init__(self, pai, titulo='Novo item', largura=350, altura=300):
        # cria uma janela FILHA do dashboard (usa o mesmo mainloop dele, não abre outra janela principal)
        super().__init__(pai)

        # guarda o dashboard pra poder usar nos outros métodos do pop-up
        self.pai = pai

        self.title(titulo) # titulo da janela
        self.geometry(f'{largura}x{altura}') # define o tamanho da janela
        self.resizable(False, False) # não deixa o usuario esticar a janela
        self.configure(fg_color=self.pai.cores["amarelo2"]) # mesma cor de fundo das outras telas

        # deixa o pop-up sempre na frente do dashboard
        self.transient(self.pai)

        # espera 100 ms a janela aparecer pra então bloquear os cliques no dashboard até o pop-up fechar
        # (chamar o grab_set direto aqui dá erro de "janela não visível")
        self.after(100, self.grab_set)

        # no windows o pop-up às vezes abre atrás do dashboard, então traz pra frente e dá o foco
        self.after(100, self.lift)
        self.after(100, self.focus)
