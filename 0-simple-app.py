import justpy as jp

def app():
    """
    Function to create a Quasar Page using the Vue.js framework from the supported components within the JustPy package.
    """
    webpage = jp.QuasarPage()
    h1 = jp.QDiv(a=webpage, text="Analysis of Course Reviews")
    p1 = jp.QDiv(a=webpage, text="These graphs represent course review analysis")
    return webpage

# Call the app function using justpy
jp.justpy(app)