from splinter.browser import Browser

def before_all(context):
    print("holaaaaaaaaaaaaaaaaaaaaaaa\n")
    context.browser = Browser()

def after_all(context):
    context.browser.quit()
    context.browser = None