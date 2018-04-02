# -*- coding: utf-8 -*-

class WebSite:
    def __init__(self, url, name):
        self.url = url
        self.name = name
        self.next_page = None
        self.prev_page = None

class Browser:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def empty(self):
        return self.head == None

    def current_page(self):
        if self.empty():
            print("No hay nada que mostrar")
        else:
            print("Página actual: {} - {}".format(self.current.name, self.current.url))

    def new_page(self, url, name):
        if self.empty():
            self.head = WebSite(url, name)
            self.tail = self.head
        else:
            node  = WebSite(url, name)
            self.tail.next_page = node
            node.prev_page = self.tail
            self.tail = node
            self.current = node

    def number_of_pages(self):
        if self.empty():
            return 0
        else:
            temp = self.head
            pages = 1
            while True:
                temp = temp.next_page
                if temp == None:
                    return pages
                else:
                    pages += 1

    def change_page(self, positions, right_or_left):
        if self.empty():
            print("No hay nada que mostrar")
        else:
            temp = self.current
            if right_or_left == 1:
                for i in range(positions):
                    temp = temp.next_page
                    if temp == None:
                        break
            elif right_or_left == 2:
                for i in range(positions):
                    temp = temp.prev_page
                    if temp == None:
                        break
            if temp != None:
                self.current = temp
                self.current_page()
            else:
                print("Imposible visitar la página")

    def historial(self):
        if self.empty():
            print("No hay páginas en el historial")
        else:
            temp = self.head
            while True:
                print("{} - {}".format(temp.name, temp.url))
                temp = temp.next_page
                if temp == None:
                    break


if __name__=="__main__":
    browser = Browser()
    browser.current_page()
    browser.new_page("www.google.cl", "Google")
    browser.new_page("www.facebook.com", "Facebook")
    browser.new_page("portal.udp.cl", "Portal UDP")
    browser.current_page()
    browser.historial()
    browser.change_page(1, 2)
    browser.change_page(1, 1)
