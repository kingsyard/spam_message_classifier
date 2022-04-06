# 0 stands for legitimate
# 1 stands for phishing

import re




#################################################################################################################################
#               Having IP address in hostname
#################################################################################################################################

def having_ip_address(url):
    match = re.search(
        '(([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\.'
        '([01]?\\d\\d?|2[0-4]\\d|25[0-5])\\/)|'  # IPv4
        '((0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\.(0x[0-9a-fA-F]{1,2})\\/)|'  # IPv4 in hexadecimal
        '(?:[a-fA-F0-9]{1,4}:){7}[a-fA-F0-9]{1,4}|'
        '[0-9a-fA-F]{7}', url)  # Ipv6
    if match:
        return 1
    else:
        return 0

#################################################################################################################################
#               URL hostname length 
#################################################################################################################################

def url_length(url):
    return len(url) 


#################################################################################################################################
#               URL shortening
#################################################################################################################################

def shortening_service(full_url):
    match = re.search('bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|'
                      'yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|'
                      'short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|'
                      'doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|'
                      'db\.tt|qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|'
                      'q\.gs|is\.gd|po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|'
                      'x\.co|prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|'
                      'tr\.im|link\.zip\.net',
                      full_url)
    if match:
        return 1
    else:
        return 0


#################################################################################################################################
#               Count at (@) symbol at base url
#################################################################################################################################

def count_at(base_url):
     return base_url.count('@')



def count_qm(base_url):
     return base_url.count('?')
 
#################################################################################################################################
#               Count comma (,) symbol at base url
#################################################################################################################################

def count_comma(base_url):
     return base_url.count(',')

#################################################################################################################################
#               Count dollar ($) symbol at base url
#################################################################################################################################

def count_dollar(base_url):
     return base_url.count('$')

#################################################################################################################################
#               Having semicolumn (;) symbol at base url
#################################################################################################################################

def count_semicolumn(url):
     return url.count(';')

#################################################################################################################################
#               Count (space, %20) symbol at base url (Das'19)
#################################################################################################################################

def count_space(base_url):
     return base_url.count(' ')+base_url.count('%20')

#################################################################################################################################
#               Count and (&) symbol at base url (Das'19)
#################################################################################################################################

def count_and(base_url):
     return base_url.count('&')


#################################################################################################################################
#               Count redirection (//) symbol at full url
#################################################################################################################################

def count_double_slash(full_url):
    list=[x.start(0) for x in re.finditer('//', full_url)]
    if list[len(list)-1]>6:
        return 1
    else:
        return 0
    return full_url.count('//')


#################################################################################################################################
#               Count slash (/) symbol at full url
#################################################################################################################################

def count_slash(full_url):
    return full_url.count('/')

#################################################################################################################################
#               Count equal (=) symbol at base url
#################################################################################################################################

def count_equal(base_url):
    return base_url.count('=')

#################################################################################################################################
#               Count percentage (%) symbol at base url (Chiew2019)
#################################################################################################################################

def count_percentage(base_url):
    return base_url.count('%')


#################################################################################################################################
#               Count exclamation (?) symbol at base url
#################################################################################################################################

def count_exclamation(base_url):
    return base_url.count('?')

#################################################################################################################################
#               Count underscore (_) symbol at base url
#################################################################################################################################

def count_underscore(base_url):
    return base_url.count('_')


#################################################################################################################################
#               Count dash (-) symbol at base url
#################################################################################################################################

def count_hyphens(base_url):
    return base_url.count('-')

#################################################################################################################################
#              Count number of dots in hostname
#################################################################################################################################

def count_dots(hostname):
    return hostname.count('.')

#################################################################################################################################
#              Count number of colon (:) symbol
#################################################################################################################################

def count_colon(url):
    return url.count(':')

#################################################################################################################################
#               Count number of stars (*) symbol (Srinivasa Rao'19)
#################################################################################################################################

def count_star(url):
    return url.count('*')

#################################################################################################################################
#               Count number of OR (|) symbol (Srinivasa Rao'19)
#################################################################################################################################

def count_or(url):
    return url.count('|')



def count_www(url):
    return url.count('www')


#################################################################################################################################
#               Path entension != .txt
#################################################################################################################################

def path_extension(url_path):
    if url_path.endswith('.txt'):
        return 1
    return 0

#################################################################################################################################
#               Having multiple http or https in url path
#################################################################################################################################

def count_http_token(url_path):
    return url_path.count('http')

#################################################################################################################################
#               Uses https protocol
#################################################################################################################################

def https_token(scheme):
    if scheme == 'https':
        return 0
    return 1

#################################################################################################################################
#               Ratio of digits in hostname 
#################################################################################################################################

def ratio_digits(hostname):
    return len(re.sub("[^0-9]", "", hostname))/len(hostname)

#################################################################################################################################
#               Count number of digits in domain/subdomain/path
#################################################################################################################################

def count_digits(line):
    return len(re.sub("[^0-9]", "", line))

#################################################################################################################################
#              Checks if tilde symbol exist in webpage URL (Chiew2019)
#################################################################################################################################

def count_tilde(full_url):
    if full_url.count('~')>0:
        return 1
    return 0


#################################################################################################################################
#               number of phish-hints in url path 
#################################################################################################################################

def phish_hints(url_path):
    count = 0
    for hint in HINTS:
        count += url_path.lower().count(hint)
    return count

#################################################################################################################################
#               Check if TLD exists in the path 
#################################################################################################################################

def tld_in_path(tld, path):
    if path.lower().count(tld)>0:
        return 1
    return 0
    
#################################################################################################################################
#               Check if tld is used in the subdomain 
#################################################################################################################################

def tld_in_subdomain(tld, subdomain):
    if subdomain.count(tld)>0:
        return 1
    return 0

#################################################################################################################################
#               Check if TLD in bad position (Chiew2019)
#################################################################################################################################

def tld_in_bad_position(tld, subdomain, path):
    if tld_in_path(tld, path)== 1 or tld_in_subdomain(tld, subdomain)==1:
        return 1
    return 0



#################################################################################################################################
#               Abnormal subdomain starting with wwww-, wwNN
#################################################################################################################################

def abnormal_subdomain(url):
    if re.search('(http[s]?://(w[w]?|\d))([w]?(\d|-))',url):
        return 1
    return 0
    

#################################################################################################################################
#               Number of redirection 
#################################################################################################################################

def count_redirection(page):
    return len(page.history)
    
#################################################################################################################################
#               Number of redirection to different domains
#################################################################################################################################

def count_external_redirection(page, domain):
    count = 0
    if len(page.history) == 0:
        return 0
    else:
        for i, response in enumerate(page.history,1):
            if domain.lower() not in response.url.lower():
                count+=1          
            return count

    
#################################################################################################################################
#               Is the registered domain created with random characters (Sahingoz2019)
#################################################################################################################################
