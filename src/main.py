import flet as ft
import mysql.connector
actualSpell = 1

def main(page: ft.Page):
   
    db = mysql.connector.connect(host="bs9ccxcowlbtszoqodoq-mysql.services.clever-cloud.com",port=3306
                                 ,user="uph3xtgfo6nvy9b8",password="wGrf5Y5alT28x7rBz4fn",database="bs9ccxcowlbtszoqodoq")
    def spellDb(spell):
        cursor = db.cursor()
        cursor.execute("UPDATE glifo SET glifoActual='" + spell + "'")
        db.commit()


    #inicia la animacion de el glifo de luz
    def animationLightSpeel(e):
        t.content = ft.Image(src=f"src/killtro.gif",width=200,height=200)
        t.update()
        global actualSpell
        actualSpell = 1
        spellDb("light")
    

    def animationIceeSpell(e):
        t.content = ft.Image(src=f"src/iceGift.gif",width=200,height=200)
        t.update()
        global actualSpell
        actualSpell = 2
        spellDb("ice")

    def animationFireSPell(e):
        t.content = ft.Image(src=f"src/fireGif.gif", width=200,height=200)
        t.update()
        global actualSpell
        actualSpell = 1
        spellDb("fire")

    


    #devuelve el hechizo anterior
    def myLastSpell():
        global actualSpell
      
        if actualSpell  == 1:
            return lightSpeell
        if actualSpell  == 2:
            actualSpell -= 1
            return lightSpeell
        if actualSpell == 3:
            actualSpell -= 1
            return iceSpeell
        if actualSpell == 4:
            actualSpell -=1
            return fireSpell
        
    #devuelve el hechizo siguiente
    def myNextSpell():
        global actualSpell
        if actualSpell == 1:
            actualSpell += 1
            return iceSpeell
        if actualSpell == 2:
            actualSpell += 1
            return fireSpell
        if actualSpell == 3:
            actualSpell += 1
            return gravitySpell
        if actualSpell == 4:
            return gravitySpell
        

    #funcionamiento del boton de regresar
    def backButtonFunc(e):
        t.content = myLastSpell()
        t.update()
    
    def nextButtonFunc(e):
        t.content = myNextSpell()
        t.update()





    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    fireSpellImage = ft.Image(src=f"src/fire.jpg",width=200,height=200)
    fireSpell = ft.ElevatedButton(content=fireSpellImage,on_click=animationFireSPell)
    gravitySpellImage = ft.Image(src=f"src/plant.jpeg")
    gravitySpell = ft.ElevatedButton(content= gravitySpellImage)
    iceSpeellImage = ft.Image(src=f"src/iceSpell.png",width=200,height=200)
    iceSpeell = ft.ElevatedButton(content=iceSpeellImage,on_click=animationIceeSpell)
    lightSpeellImage = ft.Image(src=f"src/hetoo.png",width=200,height=200)
    lightSpeell = ft.ElevatedButton(content= lightSpeellImage,on_click=animationLightSpeel)

    t = ft.AnimatedSwitcher(lightSpeell
                            ,transition=ft.AnimatedSwitcherTransition.SCALE,
        duration=500,
        reverse_duration=100,
        switch_in_curve=ft.AnimationCurve.BOUNCE_OUT,
        switch_out_curve=ft.AnimationCurve.BOUNCE_IN,)

    r = ft.Row([
        ft.ElevatedButton(text="back", on_click=backButtonFunc),
        t,
        ft.ElevatedButton(text="Next" , on_click=nextButtonFunc)
    ], alignment=ft.MainAxisAlignment.CENTER)
    page.add(r)
    

ft.app(main,assets_dir="assets")