        // Variáveis
        let tabela = document.querySelector("#corpoTabela");
        let btSalvar = document.querySelector("#btSalvar");
        let campoId = document.querySelector("#idTarefa");
        let campoNome = document.querySelector("#nomeTarefa");

        // Função que faz requisição na rota de busca por todas as tarefas e cria o elemento respectivo para cada uma, inserindo-o na tabela da página
        async function buscarTarefas() {
            let response = await fetch(urlBackEnd+"/tasks",
                                {
                                    method:"GET"
                                }
            );
            dados = await response.json();
            console.log(response.status);
            console.log(dados);
            
            tabela.innerHTML="";
            
            dados.forEach(tarefa => {
                let linha = document.createElement("tr");
                linha.innerHTML = "<td>"+tarefa["id"]+"</td>"+"<td>"+tarefa["name"]+"</td>";
                if (tarefa['done'] == false){
                    linha.innerHTML += "<td>Não</td>";
                    linha.innerHTML += "<td><a class='btn btn-success m-2' onclick='concluirTarefa("+tarefa['id']+")'>Concluir</a><a class='btn btn-primary m-2' onclick='verTarefa("+tarefa['id']+")'>Alterar</a><a class='btn btn-danger m-2' onclick='apagarTarefa("+tarefa['id']+")'>Apagar</a></td>";
                }else{
                    linha.innerHTML += "<td>Sim</td>";
                    linha.innerHTML += "<td><a class='btn btn-primary m-2' onclick='verTarefa("+tarefa['id']+")'>Alterar</a><a class='btn btn-danger m-2' onclick='apagarTarefa("+tarefa['id']+")'>Apagar</a></td>";
                }

                tabela.appendChild(linha);
            });
        }


        // Função que faz requisição na rota de cadastro de tarefa
        async function cadastrarTarefa(nomeTarefa) {

            let response = await fetch(urlBackEnd+"/tasks",
                            {
                                method : "POST",
                                headers : {"Content-Type": "application/json"},
                                body : JSON.stringify(
                                    {
                                        "name" : nomeTarefa
                                    }
                                )
                            });

            
            let dados = await response.json();
            console.log(dados);

            if(response.status == 201){
                //alert("Tarefa salva!");
                exibirToast("Sucesso","Tarefa salva!");
            }else{
                //alert(dados.detail);
                exibirToast("Falha",dados.detail);
            }

            atualizarCampos();
        }


        // Função que faz requisição na rota de edição de tarefa, passando o campo de conclusão como verdadeiro JSON
        async function concluirTarefa(idTarefa) {

            let response = await fetch(urlBackEnd+"/tasks/"+idTarefa,
                            {
                                method : "PATCH",
                                headers : {"Content-Type": "application/json"},
                                body : JSON.stringify(
                                    {
                                        "done" : true
                                    }
                                )
                            });

            
            let dados = await response.json();
            console.log(dados);

            if(response.status == 200){
                //alert("Tarefa concluída!");
                exibirToast("Sucesso","Tarefa concluída!");
            }else{
                //alert(dados.detail);
                exibirToast("Falha",dados.detail);
            }

            atualizarCampos();
        }

        // Função que faz requisição na rota de edição de tarefa
        async function editarTarefa(idTarefa,nomeTarefa) {

            let response = await fetch(urlBackEnd+"/tasks/"+idTarefa,
                            {
                                method : "PATCH",
                                headers : {"Content-Type": "application/json"},
                                body : JSON.stringify(
                                    {
                                        "name" : nomeTarefa
                                    }
                                )
                            });

            
            let dados = await response.json();
            console.log(dados);

            if(response.status == 200){
                //alert("Tarefa alterada!");
                exibirToast("Sucesso","Tarefa alterada!");
            }else{
                //alert(dados.detail);
                exibirToast("Falha",dados.detail);
            }

            atualizarCampos();
        }


        // Função que faz requisição na rota de deleção de tarefa
        async function apagarTarefa(idTarefa) {

            let response = await fetch(urlBackEnd+"/tasks/"+idTarefa,
                            {
                                method : "DELETE"
                            });

            console.log(response.status);
                            
            if(response.status == 204){
                //alert("Tarefa deletada!");
                exibirToast("Sucesso","Tarefa deletada!");
            }else{
                dados = await response.json();
                //alert(dados.detail);
                exibirToast("Falha", dados.detail);
            }

            atualizarCampos();
        }


        // Função que faz requisição na rota de busca por tarefa específica e preenche os campos com os dados obtidos
        async function verTarefa(idTarefa) {

            let response = await fetch(urlBackEnd+"/tasks/"+idTarefa,
                            {
                                method : "GET"
                            });

            let dados = await response.json();
            console.log(dados);

            if(response.status == 200){
                campoNome.value = dados.name;
                campoId.value = dados.id;
            }else{
                
                //alert(dados.detail);
                exibirToast("Falha",dados.detail);

            }
        }

        // Ao clicar no botão de salvar, chamamos a função que fará a requisição ao back-end para cadastrar ou alterar a tarefa
        btSalvar.addEventListener("click", async ()=>{
            if(campoId.value == ""){
                await cadastrarTarefa(campoNome.value);
            }else{
                await editarTarefa(campoId.value, campoNome.value);
            }
        });


        // Após a página ser carregada, chamamos a função que limpa os campos e atualiza a tabela
        document.addEventListener('DOMContentLoaded', async() => {
            await atualizarCampos();
        });
        

        // Função que limpa os campos de ID e Nome e atualiza a tabela de tarefas cadastradas
        async function atualizarCampos(){
            await buscarTarefas();
            campoNome.value="";
            campoId.value="";
        }


        // Função que define o título e a mensagem do elemento toast e exibe-o
        function exibirToast(titulo, mensagem){
            document.querySelector("#titulo").textContent = titulo;
            document.querySelector("#mensagem").textContent = mensagem;
            const toastLiveExample = document.getElementById('liveToast');
            const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
            toastBootstrap.show();
        }