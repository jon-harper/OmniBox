import load_yaml

def define_env(env):
    """
    Modifies the environment variable with new variables, macros, and filters.
    """
    from os.path import join

    env.variables.part_data = {}
    for file in env.variables.meta['bom_files']:
        load_yaml.load_yaml(env.variables.part_data, join(env.conf.docs_dir, file))

    @env.macro
    def issue_tag(issue_number : int):
        return "!!! caution \"Fit Test Pending: See Issue [#{}](https://github.com/jon-harper/OmniBox/issues/{})\"".format(issue_number, issue_number)

    @env.macro
    def product_button(url):
        return "[:material-cart: Product Link]({})".format(url) + "{ .md-button }"

    @env.macro
    def git_button(url):
        return "[:material-git: Files ][{}]".format(url) + "{ .md-button }"
    
    @env.macro
    def product_img(url, text="", width="480px"):
        return "[![{}]({})]({})".format(text, url, url)
    