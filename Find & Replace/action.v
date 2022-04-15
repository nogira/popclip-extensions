import ui
import os

struct App {
mut:
	input                  string
	find                   string
	replace                string
	is_regex               bool
	soft_input_visible     bool
	soft_input_buffer      string
	soft_input_parsed_char string
	window                 &ui.Window = voidptr(0)
}

fn main() {
	mut app := &App{
		input: 'this is a sentence\nthis is a sentence'//os.getenv("POPCLIP_FULL_TEXT")
		find : ''
		replace : ''
		is_regex : true
	}
	
	c := ui.column(
		widths: ui.stretch
		// heights: [ui.compact, ui.stretch]
		heights: ui.stretch
		margin_: 5
		spacing: 10
		children: [
			ui.row(
				spacing: 5
				height: 30
				children: [
					ui.label(
						text: 'Find' //&app.tb
						width: 50
					),
					ui.textbox(
						id: 'tb1'
						width: 180
						// height: 30
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
			ui.row(
				spacing: 5
				children: [
					// ui.label(
					// 	text: 'Regex' //&app.tb
					// 	width: 50
					// ),
					ui.checkbox(
						checked: &app.is_regex
						text: 'Regex'
					),
					ui.spacing(width: 10),
					ui.button(
						height: 20
						text: 'Replace All'
						onclick: btn_find_replace_click
					),
				]
			),
			
			
		]
	)
	w := ui.window(
		state: app
		width: 245
		height: 120
		mode: .resizable
		// on_init: init
		children: [c]
	)
	app.window = w
	ui.run(w)
}

fn btn_find_replace_click(mut app App, x voidptr) {
	// replace find with replace on input
	find := app.find
	replace := app.replace
	if app.is_regex {
		// use javascript regex bc its more known
		jsc_path := "/System/Library/Frameworks/JavaScriptCore.framework/Versions/A/Helpers/jsc"
		cmd := "'$jsc_path' -e 'print(`$app.input`.replace(/$find/gm,`$replace`))'"
		output := os.execute(cmd).output
		// remove newline
		print(output.substr(0, output.len - 1))
	} else {
		output := app.input.replace(find, replace)
		print(output)
	}
	exit(0)
}