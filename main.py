from pyscript import document, display

def order(e): 
    document.getElementById('result').innerHTML = "order"
    DHP = float(document.getElementById('DHP').value) 
    POT = float(document.getElementById('POT').value)
    GMT = float(document.getElementById('GMT').value)
    OOM = float(document.getElementById('OOM').value)
    DCT = float(document.getElementById('DCT').value)
    JBC = float(document.getElementById('JBC').value)  
    subtotal = float(DHP.value) * DHP.checked + float(POT.value) * POT.checked + float(GMT.value) * GMT.checked + float(OOM.value) * OOM.checked + float(DCT.value) * DCT.checked + float(JBC.value) * JBC.checked

    vat = subtotal * 0.12
    grandtotal = subtotal + vat

    display(f'VAT: {vat}', target='show')
    display(f'Your Total is {grandtotal}', target='show')
