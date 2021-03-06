import justpy as jp

def app():
    """
    Function to create a Quasar Page using the Vue.js framework from the supported components within the JustPy package.
    """
    webpage = jp.QuasarPage()
    jp.QDiv(a=webpage, text="Analysis of Course Reviews", classes="text-h3 text-center q-pa-md")
    jp.QDiv(a=webpage, text="These graphs represent course review analysis", classes="text-h5 text-center q-pa-md")
    return webpage

# Call the app function using justpy
jp.justpy(app)