# Atividade 1: Turtlesim: simulando um ambiente robótico integrado no ROS 

## Enunciado

Crie um script em Python capaz de interagir com o nó de simulação do turtlesim e enviar mensagens nos tópicos que regem a locomoção da tartaruga principal. Utilize este script para reproduzir um desenho de sua autoria. Utilize a estrutura de dados que preferir para representar a “imagem” a ser desenhada. O uso de programação orientada a objetos é obrigatório.

## Solução desenvolvida 
Este código é um exemplo de um controlador simples para uma simulação de robô tartaruga utilizando o ROS 2 (Robot Operating System). Ele permite que a tartaruga se mova em diferentes direções e velocidades ao longo do tempo.

A primeira parte do código é a importação dos pacotes necessários, como o Node do ROS 2 e o Twist do pacote geometry_msgs. O Node é uma classe básica do ROS 2 que permite que os desenvolvedores criem um nó para executar tarefas específicas, como publicar ou assinar tópicos. O Twist é um tipo de mensagem que contém informações de velocidade linear e angular para controlar o movimento da tartaruga.

A segunda parte do código é a criação da classe TurtleController que herda da classe Node. O método __init__ é chamado quando um objeto TurtleController é criado e define as variáveis e parâmetros necessários para controlar a tartaruga. O método create_publisher cria um publicador para publicar as mensagens Twist no tópico turtle1/cmd_vel com uma fila de tamanho 10. O método create_timer cria um temporizador com um período de 1 segundo e um retorno de chamada para o método move_turtle. O método move_turtle é onde as mensagens Twist são criadas com diferentes valores de velocidade linear e angular, dependendo do valor do contador. O método publish publica a mensagem Twist no tópico turtle1/cmd_vel.

A última parte do código é a função main, que é executada quando o script é executado diretamente. Ela inicializa o ROS 2, cria um objeto TurtleController, inicia a execução do nó com rclpy.spin(), destrói o nó e finaliza o ROS 2. O if __name__ == '__main__' verifica se o script é executado diretamente e chama a função main().

Em resumo, este código cria um nó ROS 2 que controla uma tartaruga simulada. Ele utiliza um temporizador para alterar a velocidade linear e angular da tartaruga ao longo do tempo, permitindo que ela se mova em diferentes direções e velocidades.

## Link do vídeo não listado

<a href="https://youtu.be/ZIlwc_ue9Zo">me<a\>