import flet as fl
import Client

def main(Page: fl.Page):
    Page.title = "Send Live Location (SLL)"
    Page.vertical_alignment = fl.MainAxisAlignment.CENTER

    def start_stop_send(e):
        if StaStopBut.text == "Stoped":
            StaStopBut.text = "Started"
            StaStopBut.color = "#18ea18"
            StaStopBut.bgcolor = "#000900"
            Client.asyncio.run(Client.hello())
        else:
            StaStopBut.text = "Stoped"
            StaStopBut.color = "#ff0f00"
            StaStopBut.bgcolor = "#0a0000"
        Page.update()
        
    StaStopBut = fl.Button(text = "Stoped", width = 80, height = 80,
                           color = "#ff0f00", bgcolor = "#0a0000",
                           on_click = start_stop_send)
    
    Page.add(fl.Row([StaStopBut],
             alignment = fl.MainAxisAlignment.CENTER))

fl.app(main)

