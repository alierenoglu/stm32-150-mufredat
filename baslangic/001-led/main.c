#include "stm32c0xx_hal.h"

/*
 * Kart: Nucleo-C031C6
 * Kart üzerindeki kullanıcı LED'i: PA5
 * Bu dosya görevin çözümünü içermez. GPIO ayarlarını sen tamamlayacaksın.
 */

static void MX_GPIO_Init(void)
{
    /* TODO 1: LED'in bağlı olduğu GPIO portunun saatini etkinleştir. */

    /* TODO 2: GPIO_InitTypeDef değişkenini oluştur. */

    /* TODO 3: PA5 pinini çıkış olarak ayarla ve HAL_GPIO_Init çağır. */
}

/* HAL örneğindeki SysTick kancası. İlk görevde burada işlem yok. */
void osSystickHandler(void)
{
}

int main(void)
{
    HAL_Init();
    MX_GPIO_Init();

    /* USER CODE BEGIN 2 */
    /* TODO 4: HAL ile LED'i yak. Sonra söndürmeyi de dene. */
    /* USER CODE END 2 */

    while (1)
    {
        /* USER CODE BEGIN 3 */
        /* USER CODE END 3 */
    }
}
