// Definición de pines para los componentes
int motorPin = 9;          // Pin del motor del ventilador
int waterMotorPin = 10;    // Pin del motor de agua
int ledPin = 11;           // Pin de las luces LED

void setup() {
  // Configuración de pines como salidas
  pinMode(motorPin, OUTPUT);
  pinMode(waterMotorPin, OUTPUT);
  pinMode(ledPin, OUTPUT);
  
  // Inicialización de la comunicación serial
  Serial.begin(9600);
}

void loop() {
  // Verifica si hay datos disponibles en el puerto serial
  if (Serial.available() > 0) {
    // Lee el comando enviado por el cliente Python hasta encontrar un salto de línea
    String command = Serial.readStringUntil('\n');

    // Evalúa el comando recibido y realiza la acción correspondiente
    if (command.equals("FAN_TOGGLE")) {
      toggleFanMotor();
    } else if (command.equals("WATER_TOGGLE")) {
      toggleWaterPump();
    } else if (command.startsWith("LED")) {
      controlLedIntensity(command);
    } else if (command.startsWith("FAN_SPEED")) {
      controlFanSpeed(command);
    } else {
      Serial.println("Comando desconocido");
    }
  }
}

// Función para cambiar el estado del motor del ventilador
void toggleFanMotor() {
  digitalWrite(motorPin, !digitalRead(motorPin));
  Serial.println("Motor del Ventilador Toggled");
}

// Función para cambiar el estado del motor de agua
void toggleWaterPump() {
  digitalWrite(waterMotorPin, !digitalRead(waterMotorPin));
  Serial.println("Motor de Agua Toggled");
}

// Función para ajustar la intensidad de las luces LED
void controlLedIntensity(String command) {
  // Extrae la intensidad del comando y ajusta el valor PWM en el pin correspondiente
  int intensity = command.substring(3).toInt();
  analogWrite(ledPin, map(intensity, 0, 100, 0, 255));
  Serial.println("Intensidad de LED ajustada");
}

// Función para ajustar la velocidad del motor del ventilador
void controlFanSpeed(String command) {
  // Extrae la velocidad del comando y ajusta el valor PWM en el pin correspondiente
  int speed = command.substring(9).toInt();
  analogWrite(motorPin, map(speed, 0, 100, 0, 255));
  Serial.println("Velocidad del Motor del Ventilador ajustada");
}
