humans only
===========

Flag: **can_i_borrow_a_cup_of_robots**

![humans](images/humans.png "humans only challenge introduction")

The challenge flavortext says "You shouldn't be a human for this" with a link to
<http://zeromutarts.de:8000/>, which shows a login form:

![humans login form](images/humans_login.png "humans login form")

Based on flavortext, let's visit `/robots.txt`. We find:

    User-agent: *
    Disallow: /register1337.php

    Disallow: /harming/humans
    Disallow: /ignoring/human/orders
    Disallow: /harm/to/self

Let's visit `/register1337.php`:

![humans registration page](images/humans_register.png "humans registration page")

We are presented with a registration form, so let's register with throwaway
credentials and then use them on the login page. After logging in, we see:

![humans flag](images/humans_flag.png "humans flag")

The flag is thus `can_i_borrow_a_cup_of_robots`.
