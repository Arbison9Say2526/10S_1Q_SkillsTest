from pyscript import document

def order(e): 
    item1 = float(document.getElementById('item1').value)
    item2 = float(document.getElementById('item2').value) 
    item3 = float(document.getElementById('item3').value) 
    item4 = float(document.getElementById('item4').value) 
    item5 = float(document.getElementById('item5').value)
    item6 = float(document.getElementById('item6').value) 
    subtotal = (float(item1) * document.getElementById('item1').checked + 
                float(item2) * document.getElementById('item2').checked + 
                float(item3) * document.getElementById('item3').checked + 
                float(item4) * document.getElementById('item4').checked + 
                float(item5) * document.getElementById('item5').checked + 
                float(item6) * document.getElementById('item6').checked)

    vat = subtotal * 0.12
    total = subtotal + vat
    


    document.getElementById('subtotal').innerHTML = f"{subtotal}"
    document.getElementById('vat').innerHTML = f"{vat}"
    document.getElementById('total').innerHTML = f"{total}"
