from features.base.browser import Browser

def before_all(context):
    context.browser = Browser()
    print('Now')

def after_all(context):
    context.browser.close()
    print('Done')