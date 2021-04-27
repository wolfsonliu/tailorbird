#! /usr/bin/env python3
# ------------------
# Tailorbird
# ------------------
# Author: Wolfson Liu
# Modified Date: 2021-04-27
# Version: 0.1.3
# Description:
#    Used for multiple sequence processing in GUI.
# ------------------

import tkinter as tk

__version__ = '0.1.3'

def complement(sequence):
    if not isinstance(sequence, str):
        raise ValueError('Sequence should be string.')
    atcg = {
        'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G',
        'a': 't', 't': 'a', 'g': 'c', 'c': 'g'
    }
    result = ''.join([atcg.get(x, x) for x in sequence])
    return result

def reverse_complement(sequence):
    if not isinstance(sequence, str):
        raise ValueError('Sequence should be string.')
    _comp = complement(sequence)
    result = _comp[::-1]
    return result

class Tailorbird(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.versionlabel = tk.Label(
            self,
            text='版本: {}, 邮箱: {}'.format(
                __version__, 'wolfsonliu@live.com'
            )
        )
        self.versionlabel.grid(row=0, column=0)
        self.in_textbox = self._textbox(
            '序列输入框',
            width=40, textwrap=tk.NONE,
            row=1, column=0
        )
        self.exchange_button = tk.Button(
            self,
            text='输入<=输出',
            command=self.button_exchange
        )
        self.exchange_button.grid(row=1, column=1)
        self.out_textbox = self._textbox(
            '序列输出框',
            width=40, textwrap=tk.NONE,
            row=1, column=2
        )
        self._action_buttons(row=2, column=0, columnspan=3)
        self.pack(side='top')


    def _action_buttons(self, row, column, columnspan):
        self.buttons = tk.Frame(self)
        self.buttons.grid(
            row=row, column=column, columnspan=columnspan
        )
        self.button_dict = dict()
        self.button_dict['大写'] = tk.Button(
            self.buttons, text='大写', command=self.button_upper
        )
        self.button_dict['大写'].grid(row=0, column=0)
        self.button_dict['小写'] = tk.Button(
            self.buttons, text='小写', command=self.button_lower
        )
        self.button_dict['小写'].grid(row=0, column=1)
        self.button_dict['反向互补'] = tk.Button(
            self.buttons, text='反向互补',
            command=self.button_reverse_complement
        )
        self.button_dict['反向互补'].grid(row=0, column=2)
        self.button_dict['反向'] = tk.Button(
            self.buttons, text='反向', command=self.button_reverse
        )
        self.button_dict['反向'].grid(row=0, column=3)
        self.button_dict['互补'] = tk.Button(
            self.buttons, text='互补', command=self.button_complement
        )
        self.button_dict['互补'].grid(row=0, column=4)
        self.add_head_entry = tk.Entry(
            self.buttons, width=30
        )
        self.add_head_entry.grid(row=1, column=0, columnspan=2)
        self.button_dict['添头'] = tk.Button(
            self.buttons, text='添头',
            command=self.button_add_head
        )
        self.button_dict['添头'].grid(row=1, column=2)
        self.add_tail_entry = tk.Entry(
            self.buttons, width=30
        )
        self.add_tail_entry.grid(row=1, column=3, columnspan=2)
        self.button_dict['加尾'] = tk.Button(
            self.buttons, text='加尾',
            command=self.button_add_tail
        )
        self.button_dict['加尾'].grid(row=1, column=5)


    def _textbox(self, label, width, textwrap, row, column):
        # make the text box with x and y scrollbar
        frame = tk.Frame(self)
        frame.grid(row=row, column=column)
        thelabel = tk.Label(frame, text=label)
        thelabel.grid(row=0, column=0)
        thetext = tk.Text(
            frame,
            borderwidth=3,
            width=width,
            relief=tk.SUNKEN,
            wrap=textwrap
        )
        thetext.grid(row=1, column=0)
        thescrollx = tk.Scrollbar(
            frame,
            command=thetext.xview,
            orient=tk.HORIZONTAL
        )
        thescrollx.grid(
            row=2, column=0, sticky=tk.W + tk.E + tk.N + tk.S
        )
        thetext.configure(xscrollcommand=thescrollx.set)
        thescrolly = tk.Scrollbar(
            frame,
            command=thetext.yview,
            orient=tk.VERTICAL
        )
        thescrolly.grid(
            row=1, column=1, sticky=tk.W + tk.E + tk.N + tk.S
        )
        thetext.configure(yscrollcommand=thescrolly.set)
        return thetext

    def button_exchange(self):
        # button exchange function
        output_text = self.out_textbox.get(1.0, tk.END).rstrip()
        self.in_textbox.delete(1.0, tk.END)
        self.in_textbox.insert(1.0, output_text)

    def button_add_head(self):
        entry_text = self.add_head_entry.get()
        input_text = self.in_textbox.get(
            1.0, tk.END
        ).rstrip().split('\n')
        output_text = [entry_text + x for x in input_text]
        self.out_textbox.delete(1.0, tk.END)
        self.out_textbox.insert(1.0, '\n'.join(output_text))

    def button_add_tail(self):
        entry_text = self.add_tail_entry.get()
        input_text = self.in_textbox.get(
            1.0, tk.END
        ).rstrip().split('\n')
        output_text = [x + entry_text for x in input_text]
        self.out_textbox.delete(1.0, tk.END)
        self.out_textbox.insert(1.0, '\n'.join(output_text))

    def button_upper(self):
        # button upper function
        output_text = self.in_textbox.get(
            1.0, tk.END
        ).rstrip().upper()
        self.out_textbox.delete(1.0, tk.END)
        self.out_textbox.insert(1.0, output_text)

    def button_lower(self):
        # button lower function
        output_text = self.in_textbox.get(
            1.0, tk.END
        ).rstrip().lower()
        self.out_textbox.delete(1.0, tk.END)
        self.out_textbox.insert(1.0, output_text)

    def button_reverse(self):
        # button reverse function
        input_text = self.in_textbox.get(
            1.0, tk.END
        ).rstrip().split('\n')
        output_text = [x[::-1] for x in input_text]
        self.out_textbox.delete(1.0, tk.END)
        self.out_textbox.insert(1.0, '\n'.join(output_text))

    def button_complement(self):
        # button complement function
        input_text = self.in_textbox.get(
            1.0, tk.END
        ).rstrip().split('\n')
        output_text = [complement(x) for x in input_text]
        self.out_textbox.delete(1.0, tk.END)
        self.out_textbox.insert(1.0, '\n'.join(output_text))

    def button_reverse_complement(self):
        # button reverse complement function
        input_text = self.in_textbox.get(
            1.0, tk.END
        ).rstrip().split('\n')
        output_text = [reverse_complement(x) for x in input_text]
        self.out_textbox.delete(1.0, tk.END)
        self.out_textbox.insert(1.0, '\n'.join(output_text))


if __name__ == '__main__':
    root = tk.Tk()
    root.title('Tailorbird')
    app = Tailorbird(root)
    root.mainloop()

# ------------------
# EOF
# ------------------
