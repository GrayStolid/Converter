import flet as fl

def main(Page: fl.Page):
    Page.title = "Send Live Location (SLL)"
    Page.vertical_alignment = fl.MainAxisAlignment.CENTER
    
    StaStopBut = fl.Button(text = "Start", width = 80, height = 80)
    
    Page.add(fl.Row([StaStopBut],
             alignment = fl.MainAxisAlignment.CENTER))

fl.app(main)

