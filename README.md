# Programação Orientada a Objetos II

Repositório para os materiais da disciplina POO-II.

| Código | Período | Créditos teóricos | Créditos práticos | Carga horária |
|--------|---------|-------------------|-------------------|---------------|
| SINF-CSHNB025 | 4 | 1 | 3 | 60 |

## Ementa

Ementa retirada do PPC:

- Interfaces e processamento de eventos. 
- Programação gráfica. 
- Manipulação de Arquivos. 
- Programação concorrente usando Multithreading. 
- Programação em rede. 
- Conectividade com bancos de dados: JDBC.

## Bibliografia

### Básica

#### PPC

- BARNES, D. J., KÖLLING, M. **Programação Orientada a Objetos com Java: Uma introdução prática usando BLUEJ**. 4 ed. São Paulo: Pearson Prentice Hall, 2009.
- DEITEL, H. M., DEITEL, P. J. **Java: Como programar**. 8 ed. São Paulo: Pearson Prentice Hall, 2010.
- FREEMAN, E., FREEMAN, E. **Use a Cabeça Padrões de Projetos**. 2 ed. Rio de Janeiro: Altabooks, 2007.

#### Atualizada

- PYTHON SOFTWARE FOUNDATION. **Python Programming Language**. Versão 3.14.2. Beaverton: Python Software Foundation, 2026. Disponível em: https://www.python.org/. Acesso em 29 jan. 2026.
- FITZPATRICK, Martin. **PySide6 Tutorial**. Amersfoort: Python GUI Tutorials, 2026. Disponível em: https://www.pythonguis.com/pyside6/. Acesso em 29 jan. 2026.
- PALLETS. **Flask: The Python micro framework for building web applications**. S.l.: Pallets, 2026. Disponível em: https://flask.palletsprojects.com/. Acesso em 29 jan. 2026.

### Complementar

#### PPC

- SIERRA, K.; BATES, B. **Use a Cabeça! Java**. 1 ed. Rio de Janeiro: AltaBooks, 2005.
- HORSTMANN, C. S.; CORNELL, G. **Core Java 2: Fundamentos**. 7 ed. Rio de Janeiro: Alta Books, 2005.
- KURNIAWAN, Budi. **Java para Web com Servlets, JSP e EJB**. 1 ed. Rio de Janeiro: Ciência Moderna, 2002.
- CADENHEAD, Rogers; LEMAY, Laura. **Aprenda em 21 dias Java 2**. 4 ed. Rio de Janeiro: Elsevier, 2005.
- HORSTMANN, C. **Big Java**. 4 ed. John Wiley e Sons, 2006.

#### Atualizada

- ORACLE. **MySQL**, 2026. Disponível em: https://www.mysql.com/. Acesso em: 29 jan. 2026.
- THE SQLITE CONSORTIUM. **SQLite**, 2026. Disponível em: https://sqlite.org/. Acesso em: 29 jan. 2026.
- BAYER, Michael. **SQLAlchemy - The Database Tookit for Python**, 2026. Disponível em: https://www.sqlalchemy.org/. Acesso em: 29 jan. 2026.

## Conteúdo Programático

### Unidade 1 - Interfaces, Eventos e Programação Gráfica

- PySide6
	- Introdução.
	- Sinais, *Slots* & Eventos.
	- Widgets.
	- Layouts.
	- Barras de ferramentas e Menus --- QAction.
	- *Dialogs* e *Alerts*.
	- Criando janelas adicionais.

### Unidade 2 - Arquivos e Multithreading

- Arquivos em Python
- Threads em Python.
- Serialização de dados: CSV e JSON.
- PySide6 
	- Multithreading com `QThreadPool`.
	- Executando programas externos com `QProcess`.

### Unidade 3 - Programação em Rede e Banco de Dados

- Noções básicas de rede
	- Flask.
	- Docker.
- Banco de dados
	- SQLite.
	- MySQL.
	- SQLAlchemy.
- Integração GUI + Rede + Banco.

## Avaliação

Ao **fim de cada unidade**, será realizada uma **avaliação parcial** dos conteúdos ministrados durante o curso da unidade, <span style="color:red;font-weight: bold;">totalizando em 03 (três) avaliações</span>.

A **nota de cada avaliação** poderá ser **composta por um ou mais instrumentos de avaliação**, de acordo com um dos seguintes casos:

1. Uma prova escrita.
2. Um ou mais trabalhos (individuais ou em grupo).
3. Um ou mais trabalhos, mais uma prova escrita.

Nos casos em que a **avaliação** seja **composta por mais de um instrumento**, será realizado o **somatório** ou a **média ponderada** das **notas obtidas em cada instrumento** para compor a **nota final** de uma **avaliação parcial**.

Os instrumentos a serem utilizados em cada avaliação serão definidos e informados no decorrer do curso.

As **notas** obedecem a uma escala de **0,0 (zero)** a **10,0 (dez)**, contando até a primeira ordem decimal com possı́veis arredondamentos.

Considerar-se-á **aprovado** na disciplina o aluno que obtiver **assiduidade igual ou superior a 75%** e a média **aritmética igual ou superior a 7,0 (sete)** nas <u>avaliações parciais (média parcial)</u>, ou que se submeta a exame final e obtenha média aritmética (média final) entre a média parcial e exame final igual ou superior a 6,0 (seis).

Terá direito de realizar exame final o aluno que satisfaça os requisitos de assiduidade e que obtenha média parcial maior ou igual a 4,0 (quatro) e menor que 7,0 (sete).

### Faltas

As faltas poderão ser justificadas a partir de algum documento que comprove o motivo da falta. Os motivos incluem, mas não se limitam a:

- Choques de horário com outra atividade acadêmica.
- Choques de horário com atividade remunerada (trabalho).
- Questões de saúde.

O documento deve ser enviado para o e-mail <a href="mailto:evandro.silva@ufpi.edu.br">evandro.silva@ufpi.edu.br</a>. O campo **assunto** deverá ser preenchido da seguinte forma: `POO 2 - [Atestado|Declaração] para falta no dia DD/MM`. <span style="color:red;font-weight: bold;">O abono da falta ocorrerá somente ao fim do semestre letivo</span>.

## Calendário

<link rel="stylesheet" href="calendario.css">

<!--<span style="background-color:#32cd32;color:white;padding:5px 10px;"><b>AULA</b></span>-->
<span class="badge aula">AULA</span>
<span class="badge feriado">FERIADO</span>
<span class="badge prova">PROVA</span>

<div class="tabelas">
  <table class="calendario">
  	<thead>
  		<tr><th colspan="5">Março</th></tr>
  		<tr>
  			<th>Seg</th>
  			<th>Ter</th>
  			<th>Qua</th>
  			<th>Qui</th>
  			<th>Sex</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td>02</td>
  			<td>03</td>
  			<td>04</td>
  			<td>05</td>
  			<td>06</td>
  		</tr>
  		<tr>
  			<td>09</td>
  			<td class="aula" conteudo="PySide6: Introdução; Sinais, Slots & Eventos; Widgets.">10</td>
  			<td>11</td>
  			<td>12</td>
  			<td class="aula" conteudo="Prática">13</td>
  		</tr>
  		<tr>
  			<td>16</td>
  			<td class="aula" conteudo="PySide6: Layouts; Barras de ferramentas e Menus.">17</td>
  			<td>18</td>
  			<td>19</td>
  			<td class="aula" conteudo="Prática">20</td>
  		</tr>
  		<tr>
  			<td>23</td>
  			<td class="aula" conteudo="PySide6: Dialogs e Alerts; Criando janelas adicionais.">24</td>
  			<td>25</td>
  			<td>26</td>
  			<td class="aula" conteudo="Prática">27</td>
  		</tr>
  		<tr>
  			<td>30</td>
  			<td class="prova" conteudo="AV1">31</td>
  			<td></td>
  			<td></td>
  			<td></td>
  		</tr>
  	</tbody>
  </table>

  <table class="calendario">
  	<thead>
  		<tr><th colspan="5">Abril</th></tr>
  		<tr>
  			<th>Seg</th>
  			<th>Ter</th>
  			<th>Qua</th>
  			<th>Qui</th>
  			<th>Sex</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td></td>
  			<td></td>
  			<td>01</td>
  			<td>02</td>
  			<td class="feriado" conteudo="Sexta-feira da paixão">03</td>
  		</tr>
  		<tr>
  			<td>06</td>
  			<td class="aula" conteudo="Arquivos em Python">07</td>
  			<td>08</td>
  			<td>09</td>
  			<td class="aula" conteudo="Prática">10</td>
  		</tr>
  		<tr>
  			<td>13</td>
  			<td class="aula" conteudo="Threads em Python">14</td>
  			<td>15</td>
  			<td>16</td>
  			<td class="aula" conteudo="Prática">17</td>
  		</tr>
  		<tr>
  			<td>20</td>
  			<td class="feriado" conteudo="Tiradentes">21</td>
  			<td>22</td>
  			<td>23</td>
  			<td class="aula" conteudo="Serialização de dados: CSV e JSON.">24</td>
  		</tr>
  		<tr>
  			<td>27</td>
  			<td class="aula" conteudo="Prática">28</td>
  			<td>29</td>
  			<td>30</td>
  			<td></td>
  		</tr>
  	</tbody>
  </table>

  <table class="calendario">
  	<thead>
  		<tr><th colspan="5">Maio</th></tr>
  		<tr>
  			<th>Seg</th>
  			<th>Ter</th>
  			<th>Qua</th>
  			<th>Qui</th>
  			<th>Sex</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td></td>
  			<td></td>
  			<td></td>
  			<td></td>
  			<td class="feriado" conteudo="Dia do Trabalho">01</td>
  		</tr>
  		<tr>
  			<td>04</td>
  			<td class="aula" conteudo="PySide6: Multithreading">05</td>
  			<td>06</td>
  			<td>07</td>
  			<td class="aula" conteudo="PySide6: Execução de programas externos">08</td>
  		</tr>
  		<tr>
  			<td>11</td>
  			<td class="aula" conteudo="Prática">12</td>
  			<td>13</td>
  			<td>14</td>
  			<td class="prova" conteudo="AV2">15</td>
  		</tr>
  		<tr>
  			<td>18</td>
  			<td class="prova" conteudo="AV2">19</td>
  			<td>20</td>
  			<td>21</td>
  			<td class="aula" conteudo="Noções básicas de rede + Flask">22</td>
  		</tr>
  		<tr>
  			<td>25</td>
  			<td class="aula" conteudo="Docker">26</td>
  			<td>27</td>
  			<td>28</td>
  			<td class="aula" conteudo="Prática">29</td>
  		</tr>
  	</tbody>
  </table>

  <table class="calendario">
  	<thead>
  		<tr><th colspan="5">Junho</th></tr>
  		<tr>
  			<th>Seg</th>
  			<th>Ter</th>
  			<th>Qua</th>
  			<th>Qui</th>
  			<th>Sex</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td>01</td>
  			<td class="aula" conteudo="Banco de dados: revisão">02</td>
  			<td>03</td>
  			<td class="feriado" conteudo="Corpus Christi">04</td>
			<td style="background-image: repeating-linear-gradient(135deg, #32cd32, #32cd32 10px, #6495ed 10px, #6495ed 20px);" conteudo="Ponto facultativo / Prática">05</td>
  		</tr>
  		<tr>
  			<td>08</td>
  			<td class="aula" conteudo="Conexão com banco de dados">09</td>
  			<td>10</td>
  			<td>11</td>
  			<td class="aula" conteudo="Prática">12</td>
  		</tr>
  		<tr>
  			<td>15</td>
  			<td class="aula" conteudo="ORM: SQLAlchemy">16</td>
  			<td>17</td>
  			<td>18</td>
  			<td class="aula" conteudo="Prática">19</td>
  		</tr>
  		<tr>
  			<td>22</td>
  			<td class="aula" conteudo="Prática">23</td>
  			<td>24</td>
  			<td>25</td>
  			<td class="prova" conteudo="AV3">26</td>
  		</tr>
  		<tr>
  			<td>29</td>
  			<td class="prova" conteudo="AV3">30</td>
  			<td></td>
  			<td></td>
  			<td></td>
  		</tr>
  	</tbody>
  </table>

  <table class="calendario">
  	<thead>
  		<tr><th colspan="5">Julho</th></tr>
  		<tr>
  			<th>Seg</th>
  			<th>Ter</th>
  			<th>Qua</th>
  			<th>Qui</th>
  			<th>Sex</th>
  		</tr>
  	</thead>
  	<tbody>
  		<tr>
  			<td></td>
  			<td></td>
  			<td>01</td>
  			<td>02</td>
			<td class="aula" conteudo="Livre">03</td>
  		</tr>
  		<tr>
  			<td>06</td>
  			<td class="prova" conteudo="Avaliação Final">07</td>
  			<td>08</td>
  			<td>09</td>
  			<td>10</td>
  		</tr>
  		<tr>
  			<td>13</td>
  			<td>14</td>
  			<td>15</td>
  			<td>16</td>
  			<td>17</td>
  		</tr>
  		<tr>
  			<td>20</td>
  			<td>21</td>
  			<td>22</td>
  			<td>23</td>
  			<td>24</td>
  		</tr>
  		<tr>
  			<td>27</td>
  			<td>28</td>
  			<td>29</td>
  			<td>30</td>
  			<td>31</td>
  		</tr>
  	</tbody>
  </table>
</div>

<!--
<div class="tabelas">
  <ul style="padding: 15px;margin:0;max-width: 200px;">
	<li><b>10</b>: PySide6
		<ul>
			<li>Introdução.</li>
			<li>Sinais, <i>Slots</i> & Eventos.</li>
			<li>Widgets.</li>
		</ul>
	</li>
	<li><b>13</b>: Prática</li>
	<li><b>17</b>: PySide6
		<ul>
			<li>Layouts.</li>
			<li>Barras de ferramentas e Menus.</li>
		</ul>
	</li>
	<li><b>20</b>: Prática</li>
	<li><b>24</b>: PySide6
		<ul>
			<li><i>Dialogs</i>, <i>Alerts</i> e criação de janelas adicionais.</li>
		</ul>
	</li>
	<li><b>27</b>: Prática</li>
	<li><b>31</b>: AV1</li>
  </ul>

  <ul style="padding: 10px;margin:0;max-width: 200px;">
	<li><b>10</b>: PySide6
		<ul>
			<li>Introdução.</li>
			<li>Sinais, <i>Slots</i> & Eventos.</li>
			<li>Widgets.</li>
		</ul>
	</li>
	<li><b>13</b>: Prática</li>
	<li><b>17</b>: PySide6
		<ul>
			<li>Layouts.</li>
			<li>Barras de ferramentas e Menus.</li>
		</ul>
	</li>
	<li><b>20</b>: Prática</li>
	<li><b>24</b>: PySide6
		<ul>
			<li><i>Dialogs</i>, <i>Alerts</i> e criação de janelas adicionais.</li>
		</ul>
	</li>
	<li><b>27</b>: Prática</li>
	<li><b>31</b>: AV1</li>
  </ul>
</div>
-->