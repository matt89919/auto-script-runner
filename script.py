script='''
var element = document.querySelectorAll("body *") // All element in body
var pageWidth = document.documentElement.scrollWidth
var pageHeight = document.documentElement.scrollHeight
var windowWidth = window.innerWidth
var windowHeight = window.innerHeight
var toShow = document.createElement("div")

console.log(windowWidth, windowHeight)
console.log(pageWidth, pageHeight)

function drawRect(el,color) 
{
	let rect = el.getBoundingClientRect();
	// console.log(rect.height);
	// console.log(rect.width);
	//console.log("stop");
    let showdivEle = document.createElement("div");
    showdivEle.style.visibility = "visible";
    showdivEle.style.top = rect.y+ "px";
    showdivEle.style.left = rect.x + "px";
    showdivEle.style.position = "fixed";
    showdivEle.style.height = rect.height + "px";
    showdivEle.style.width = rect.width + "px";
    showdivEle.style.border = "3px solid " + color;
    showdivEle.style.zIndex = "2147483646";
    showdivEle.title = rect.content;
    toShow.appendChild(showdivEle);
    //console.log(rect.x);
    //console.log(rect.y);
}

function checkscroll(element)
{
	let result = false;

	for(let i = 0; i < element.length; i++)
	{
	    if(element[i].clientWidth > pageWidth+1  && element[i].clientHeight > 0)
	    {
	        //console.log(element[i].localName, element[i].clientWidth, 
	        //	element[i].scrollHeight);
			let style = window.getComputedStyle(element[i]);
			console.log(element[i].localName ,style.overflowX);
			if(style.overflowX != "scroll")
			{
				result = true;
				drawRect(element[i],"Red");
			}
	        
	    }
	    if(element[i].clientHeight > pageHeight+1 && element[i].clientWidth > 0)
	    {
	    	//console.log(element[i].localName, element[i].clientWidth, 
	       	//element[i].scrollHeight);
			let style = window.getComputedStyle(element[i]);
			console.log(element[i].localName ,style.overflowY);
			if(style.overflowY != "scroll")
			{
				result = true;
				drawRect(element[i],"Green");
			}

	    }
	}
	return result;
}

document.body.appendChild(toShow); // 將 Rectangle 加入 body 中顯示
return checkscroll(element);
''' 