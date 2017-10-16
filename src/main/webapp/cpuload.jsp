<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=GBK">
<title>CPULoad</title>
</head>
<script src="jquery-2.1.1.js"></script>
<script type="text/javascript">

	function add(){
		var num=document.getElementById ("num").value;
		$.ajax({
			type: 'POST',
			url: '${pageContext.request.contextPath}/servlet/addServlet',
			data:{
				"num":num
			},
			dataType: 'text',
			success:function(obj){
				$("#addcount").text(obj.toString());
				document.getElementById ("num").value=''
			}
		});
	}

	function reduce(){
		var num=document.getElementById ("num2").value;
		$.ajax({
			type: 'POST',
			url: '${pageContext.request.contextPath}/servlet/reduceServlet',
			data:{
				"num":num
			},
			dataType: 'text',
			success:function(obj){
				$("#redcount").text(obj.toString());
				document.getElementById ("num2").value=''
			}
		});
	}
	function getenv(){
		$.ajax({
			type: 'POST',
			url: '${pageContext.request.contextPath}/servlet/getEnvServlet',
			dataType: 'text',
			success:function(obj){
			    var arrayObj = new Array();
			    var arrayObj = obj.toString().split(",");
			    var  envdiv = $("#envval");
			    for(var i=0;i<arrayObj.length;i++){
			      envdiv.append("<li>"+arrayObj[i]+"</li>");
			    }
			}
		});
	}
	function getcpuval(){
		$.ajax({
			type: 'POST',
			url: '${pageContext.request.contextPath}/servlet/getCpuRatioServlet',
			dataType: 'text',
			success:function(obj){
			    $("#cpucon").text(obj.toString());
			}
		});
	}

</script>
<body>
<%
		Cookie[] cks = request.getCookies();
		Cookie authCookie = null;
		if (cks != null) {
			for (int i = 0; i < cks.length; i++) {
				String name = cks[i].getName();
				System.out.println(name);
				if (name.equals("auth")) {
					authCookie = cks[i];
					break; // exit the loop and continue the page
				}
			}
			if (authCookie == null)
			{
				RequestDispatcher disp = request.getRequestDispatcher(request.getContextPath() + "/cpuload.jsp");
				disp.forward(request, response);
				return;
			}
		} else {
			RequestDispatcher disp = request.getRequestDispatcher(request.getContextPath() + "/cpuload.jsp");
			disp.forward(request, response);
			response.sendRedirect("index.jsp");
			return; // to stop further execution
		}
	%>

        <div> Version 1
        </div>
        <p>Welcome: <%=authCookie.getValue()%>.
	<div>
		<input type="button" id="addButton" onClick="add()" value="增加"/>
		<input type="text" id="num"></input>
		<span>&nbsp;&nbsp;</span>
	    <span id="addcount"></span>
	</div>
	<br/>
	<div>
		<input type="button" id="reduceButton" onClick="reduce()" value="减少"/>
		<input  type="text" id="num2"></input>
		<span>&nbsp;&nbsp;</span>
	    <span id="redcount"></span>
	</div>
	<br/>
	<div>
		<input type="button" id="cpuval" onClick="getcpuval()" value="CPU%"/>
		<span>&nbsp;&nbsp;</span>
	     <span id="cpucon"></span>
	</div>
	<br/>
	<div>
		<input type="button" id="env" onClick="getenv()" value="环境变量"/>
		<div id="envval"></div>
	</div>

</body>
</html>
