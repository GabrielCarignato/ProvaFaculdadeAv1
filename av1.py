from abc import ABC, abstractmethod

class Canal(ABC):
    def __init__(self, destinatario):
        self.destinatario = destinatario

    @abstractmethod
    def enviar_mensagem(self, mensagem):
        pass

class Mensagem(ABC):
    def __init__(self, conteudo, formato):
        self.conteudo = conteudo
        self.formato = formato

    @abstractmethod
    def enviar(self):
        pass

class WhatsApp(Canal):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem para {self.destinatario} via WhatsApp: {mensagem.conteudo}")

class Telegram(Canal):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem para {self.destinatario} via Telegram: {mensagem.conteudo}")

class Facebook(Canal):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem para {self.destinatario} via Facebook: {mensagem.conteudo}")

class Instagram(Canal):
    def enviar_mensagem(self, mensagem):
        print(f"Enviando mensagem para {self.destinatario} via Instagram: {mensagem.conteudo}")

class MensagemTexto(Mensagem):
    def __init__(self, conteudo, formato, data_envio):
        super().__init__(conteudo, formato)
        self.data_envio = data_envio

    def enviar(self):
        print(f"Enviando mensagem de texto: {self.conteudo}, Enviada em: {self.data_envio}")

class MensagemVideo(Mensagem):
    def __init__(self, conteudo, formato, duracao):
        super().__init__(conteudo, formato)
        self.duracao = duracao

    def enviar(self):
        print(f"Enviando vídeo: {self.conteudo}, Formato: {self.formato}, Duração: {self.duracao} segundos")

class MensagemFoto(Mensagem):
    def enviar(self):
        print(f"Enviando foto: {self.conteudo}, Formato: {self.formato}")

class MensagemArquivo(Mensagem):
    def enviar(self):
        print(f"Enviando arquivo: {self.conteudo}, Formato: {self.formato}")

whatsapp = WhatsApp("+55110000000")
telegram = Telegram("@usuario_telegram")
facebook = Facebook("Nome do Amigo")
instagram = Instagram("@usuario_instagram")

mensagem_texto = MensagemTexto("Olá, como vai?", "Texto", "2023-12-04")
mensagem_video = MensagemVideo("Aniversário", "MP4", 30)
mensagem_foto = MensagemFoto("Paisagem", "JPEG")
mensagem_arquivo = MensagemArquivo("Documento", "PDF")

whatsapp.enviar_mensagem(mensagem_texto)
telegram.enviar_mensagem(mensagem_video)
facebook.enviar_mensagem(mensagem_foto)
instagram.enviar_mensagem(mensagem_arquivo)




#Código feito para Avaliação da faculdade.
        