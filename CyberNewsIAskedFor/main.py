from cybernews.cybernews import CyberNews
import cybernews 
import fontstyle



# print(dir(report))
# -----------------------------------------------------------
# this gives out list it seems ~TypeError: list indices must be integers or slices, not str
def _select_category(category):
    """Creates a Instance of the CyberNews and SELECTS the mentioned category and Returns it"""
    news = CyberNews()
    _categoryContent = news.get_news(category)
    return _categoryContent
# -----------------------------------------------------------
# figured out, That the .json is listed. 
# before accessing .json, index to that particular .json
# print(_categoryContent[0].get('headlines')) [ {.json}, {.json} ,{.json} ...]
# -----------------------------------------------------------
# This much NEWS is sent under the specified category
# print(len(_categoryContent))
# -----------------------------------------------------------
# 30 Headlines 
# 31 Headlines More
# this list headlines of all the news under that particular news category.
# for title in range(len(_categoryContent)):
#     print(f"{title + 1} {_categoryContent[title].get('headlines')}")
# -----------------------------------------------------------
# list of possible news categories
'''
| 1 | General News | news.get_news("general") |
| 2 | Data Breach News | news.get_news("dataBreach") |
| 3 | Cyber Attack News | news.get_news("cyberAttack") |
| 4 | Vulnerability News | news.get_news("vulenrability")|
| 5 | Malware News | news.get_news("malware") |
| 6 | Security News | news.get_news("security") |
| 7 | Cloud News | news.get_news("cloud") |
| 8 | Tech News | news.get_news("tech") |
| 9 | IOT News | news.get_news("iot") |
| 10 | Big Data News | news.get_news("bigData") |
| 11 | Business News | news.get_news("business") |
| 12 | Mobility News | news.get_news("mobility") |
| 13 | Research News | news.get_news("research") |
| 14 | Corporate News | news.get_news("corporate") |
| 15 | Social Media News | news.get_news("socialMedia") |
'''
# ----------------------------------------------------------------------------
# # ? Ser.NO  DataOfNews  News-HeadLines  >> also it Prints the content in BLUE color
# var = select_category("security")
# print(type(var))
# for title in range(len(var)):
#     print(fontstyle.apply(f"{title + 1} On {var[title].get('newsDate')}, {var[title].get('fullNews')}",'bold/Italic/blue' ))
# ----------------------------------------------------------------------------


# ----------------------------------------------------------------------------
# # ? Ser.NO  DataOfNews  News-HeadLines  >> also it Prints the content in BLUE color
# securityNews = _select_category("security")
# # print(type(var))
# for news in securityNews:
#     print(fontstyle.apply(f" On {news.get('newsDate')}, {news.get('headlines')}",'bold/Italic/blue' ))
#     print("\n")
# ----------------------------------------------------------------------------


# =================================================================================
# all from perticular categories
# def print_all_contents_of(this,fromThis,withColor="blue"):
#     """Interface for the content Printing.!!   from a categoryContent. """
#     _newsContent = _select_category(fromThis)
#     print(f"""News From: \"{fromThis}\"""")
#     for news in _newsContent:
#         print(fontstyle.apply(f"{news.get(this)}",f'bold/{withColor}' ))
# =================================================================================


# =================================================================================
# enumerate does the traversing and counting along with it.
def print_all_contents_of(this,fromThis,withColor="blue"):
    """Interface for the content Printing.!!   from a categoryContent. """
    _newsContent = _select_category(fromThis)
    print(f"""News From: \"{fromThis}\"""")
    for serial,news in enumerate(_newsContent):
        print(fontstyle.apply(f"{serial + 1} {news.get(this)}",f'bold/{withColor}' ))
# =================================================================================

# '/news/cybercrime-fraud/ {lockbit-ransomware-gang-hits-indias-national-aerospace-laboratories} /105579299'
# _categoryContent[index].get('newsURL')
# simple code to strip TITLE
# def get_title(newsURL):
#     print(newsURL.split("/")[2])
# later dropped idea because, not every time the URL like this vague.

# =================================================================================
# this based on the category prints either latest or Top Five News.
def print_news_from(category,latest=True):
    """Prints news from the given category based on weather latest or not
        if latest just prints LATEST i.e top 2 news
        if not latest prints TOPNEWS i.e top 5 news """
    _TOPNEWS = 5
    _LATEST = 2 
    """Improvement would be, to fetch the news based on TIME i.e to compare the dates 
    and decide for accurate latest news"""


    _newsContent = _select_category(category)
    if not latest:
        print(f"""
    
    Here are TOP FIVE News on \"{category}\"""")
        for _serial, news in enumerate(_newsContent):
            if _serial == _TOPNEWS:
                break
            print(f"""
                    ------------------------------------------------------------------
                    {fontstyle.apply(f"{news.get('headlines')}",'bold/Italic/blue')}
                    {fontstyle.apply(f"date: {news.get('newsDate')}",'faint/Italic')}
                    {fontstyle.apply(f"{news.get('newsURL')}",'white/blue_bg/Italic')}

                    {fontstyle.apply(f"{news.get('fullNews')}",'black/white_bg')}
                    """)
    else:
        print(f"""
    
    Here are LATEST News on \"{category}\"""")
        for _serial, news in enumerate(_newsContent):
            if _serial == _LATEST:
                break
            print(f"""
                    ------------------------------------------------------------------
                    {fontstyle.apply(f"{news.get('headlines')}",'bold/Italic/blue')}
                    {fontstyle.apply(f"date: {news.get('newsDate')}",'faint/Italic')}
                    {fontstyle.apply(f"{news.get('newsURL')}",'white/blue_bg/Italic')}

                    {fontstyle.apply(f"{news.get('fullNews')}",'black/white_bg')}
                    """)
# =================================================================================


# =================================================================================
# program starts here..

"""
FUTURE SCOPE:
One Major improvement can be, not to ask any category and all, 
giving THE LATEST news automatically searching from across various domains

for instance:  __interface would be like__

THE LATEST cybernews, from ANY CATEGORY !! (__Automatically, Not even have to Enter anything__)
(when i say latest, its based on relative TIME, more recent the INCIDENT more LATEST it is)
"""
if __name__ == "__main__":
    # print_all_contents_of("headlines",fromThis="security",withColor="red")

    print_news_from('malware',latest=True)