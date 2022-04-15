import ui
import os

struct App {
mut:
	input                  string
	find                   string
	replace                string
	soft_input_visible     bool
	soft_input_buffer      string
	soft_input_parsed_char string
	window                 &ui.Window = voidptr(0)
}

fn main() {
	mut app := &App{
		input: os.getenv("POPCLIP_FULL_TEXT")
		find : ''
		replace : ''
	}
	
	c := ui.column(
		widths: ui.stretch
		heights: [ui.compact, ui.stretch]
		margin_: 5
		spacing: 10
		children: [
			ui.row(
				spacing: 5
				children: [
					ui.label(
						text: 'Find' //&app.tb
						width: 50
					),
					ui.textbox(
						id: 'tb1'
						width: 180
						//mode: .multiline | .word_wrap
						text: &app.find
						// fitted_height: true
					),
				]
			),
			ui.row(
				spacing: 5
				children: [
					ui.label(
						text: 'Replace' //&app.tb
						width: 50
					),
					ui.textbox(
						id: 'tb2'
						width: 180
						//mode: .multiline | .word_wrap
						text: &app.replace
						// fitted_height: true
					),
				]
			),
			ui.button(
				text: 'Ok'
				onclick: btn_find_replace_click
			),
			
		]
	)
	w := ui.window(
		state: app
		width: 250
		height: 100
		mode: .resizable
		// on_init: init
		children: [c]
	)
	app.window = w
	ui.run(w)
}

fn btn_find_replace_click(mut app App, x voidptr) {
	// replace find with replace on input
	find := app.find.replace('\\n', '\n')
					.replace('\\t', '\t')
	replace := app.replace.replace('\\n', '\n')
						.replace('\\t', '\t')
	output := app.input.replace(find, replace)
	print(output)
	exit(0)
}