function getPrintWindow() {
    var f = this.Iframe()
    return {
        f: f,
        win: f.contentWindow || f,
        doc: f.doc,
    }
}

function Iframe() {
    let frameId = "printArea"
    let url = new Date().getTime()

    let iframe = document.createElement("iframe")
    iframe.style.border = "0px"
    iframe.style.position = "absolute"
    iframe.style.width = "0px"
    iframe.style.height = "0px"
    iframe.style.right = "0px"
    iframe.style.top = "0px"
    iframe.setAttribute("id", frameId)
    iframe.setAttribute("src", url)

    document.body.appendChild(iframe)
    iframe.doc = null
    iframe.doc = iframe.contentDocument
        ? iframe.contentDocument
        : iframe.contentWindow
        ? iframe.contentWindow.document
        : iframe.document
    return iframe
}

let style = "@page{size: auto; margin: 0;}"
let head = `<head><title>Print</title><style type="text/css">${style}</style></head>`
let body = "<body>" + document.getElementById("printMe").outerHTML + "</body>"
let html = `<!DOCTYPE html><html>${head}${body}</html>`

let PADocument = getPrintWindow().doc
PADocument.open()
PADocument.write(html)
PADocument.close()

document.getElementById("printArea").focus()
document.getElementById("printArea").contentWindow.print()