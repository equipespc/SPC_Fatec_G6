var pesquisar = document.getElementById("pesquisa");
var strCPF = document.getElementById("cpf");
var numCPF = document.getElementById("numCPF");
var dadosCPF = document.getElementById("dados");
// var modais = document.getElementByClassName("modal fade");

pesquisar.addEventListener("click", function () {
  var input;
  console.log("funciona");
  console.log(strCPF.value);

  // function ativaModal() {
  //   pesquisar.setAttribute("data-target", "#tabela_modal");
  // }

  function TestaCPF(input) {
    input = strCPF.value;
    var valido = 0;
    var Soma;
    var Resto;
    Soma = 0;
    //strCPF  = RetiraCaracteresInvalidos(strCPF,11);
    if (input == "00000000000") {
      // console.log("funcionando1");
      numCPF.append(document.createTextNode("CPF invalido"));
      return false;
    }
    for (i = 1; i <= 9; i++)
      Soma = Soma + parseInt(input.substring(i - 1, i)) * (11 - i);
    Resto = (Soma * 10) % 11;
    if (Resto == 10 || Resto == 11) Resto = 0;
    if (Resto != parseInt(input.substring(9, 10))) {
      //console.log("funcionando2");
      numCPF.append(document.createTextNode("CPF invalido"));
      return false;
    }
    Soma = 0;
    for (i = 1; i <= 10; i++)
      Soma = Soma + parseInt(input.substring(i - 1, i)) * (12 - i);
    Resto = (Soma * 10) % 11;
    if (Resto == 10 || Resto == 11) Resto = 0;
    if (Resto != parseInt(input.substring(10, 11))) {
      //console.log("funcionando3");
      numCPF.append(document.createTextNode("CPF invalido"));
      return false;
    }
    //console.log("funcionando4");
    //numCPF.append(document.createTextNode("CPF valido"));

    valido = 1;

    switch (valido == 1) {
      case input == "01367130760":
        pesquisar.setAttribute("data-target", "#01367130760");
        dadosCPF.append(
          document.createTextNode("Você atrasou o pagamento em 2 meses")
        );

        break;

      case input == "05227401381":
        pesquisar.setAttribute("data-target", "#05227401381");
        dadosCPF.append(
          document.createTextNode("Você atrasou o pagamento em 1 mês")
        );
        break;

      case input == "05309680888":
        pesquisar.setAttribute("data-target", "#05309680888");
        dadosCPF.append(
          document.createTextNode("Você atrasou o pagamento em 8 meses")
        );
        break;
      case input == "09639103101":
        pesquisar.setAttribute("data-target", "#09639103101");
        dadosCPF.append(
          document.createTextNode("Você atrasou o pagamento em 10 meses")
        );
        break;
      case input == "24048813021":
        pesquisar.setAttribute("data-target", "#24048813021");
        dadosCPF.append(
          document.createTextNode("Você atrasou o pagamento em 3 meses")
        );
        break;

      default:
        dadosCPF.append(
          document.createTextNode("Seu CPF não está no nosso sistema.")
        );
        return true;
        break;
      /*   case input == "18106900800":
        pesquisar.setAttribute("data-target", "#18106900800");
        dadosCPF.append(
          document.createTextNode("Você atrasou o pagamento em 6 meses")
        );
        break;
      case input == "12731112573":
        pesquisar.setAttribute("data-target", "#12731112573");
        dadosCPF.append(
          document.createTextNode("Você atrasou o pagamento em 7 meses")
        );
        break;
      case input == "28537130320":
        pesquisar.setAttribute("data-target", "#28537130320");
        dadosCPF.append(
          document.createTextNode("Você atrasou o pagamento em 8 meses")
        );
        break;
        */
    }

    return true;
  }
  TestaCPF();
});
