# CFLT Part I — Logic Transformer Benchmark

**Generated:** 2026-05-17 10:51:44  
**DX runs per case:** 1  
**SC** Slot order (Core→Reason→Space→Time)  
**SR** Subject retained in Core  
**IV** Inferred slots have suggestions  
**DX** Downstream extraction accuracy on transformer-generated CFLT

> Part II baselines: L3 ctrl ≈65%  / L3 human-CFLT = 100%.  A good transformer should bring DX close to the human ceiling.


## Transformer: `deepseek/deepseek-v4-pro`  |  Extractor: `openai/gpt-5`

### Per-case results

| ID | L | Lang | SC | SR | IV | DX | CFLT text preview |
| :-- | :- | :-- | :-- | :-- | :-- | :-- | :-- |
| EN_L1_01 | 1 | en | ✅ | ✅ | ✅ | 1.00 | close the window, because it is raining outside, inside, now |
| EN_L1_02 | 1 | en | ✅ | ✅ | ✅ | 1.00 | turn off the stove, because the water is boiling, in the kit |
| EN_L1_03 | 1 | en | ✅ | ✅ | ✅ | 1.00 | feed it, because the dog is hungry, at home, now. |
| ZH_L1_01 | 1 | zh | ✅ | ✅ | ✅ | 1.00 | 把窗户关上，因为外面下雨了，在屋里，现在。 |
| ZH_L1_02 | 1 | zh | ✅ | ✅ | ✅ | 1.00 | 关掉炉子，因为水开了，在厨房，现在。 |
| ZH_L1_03 | 1 | zh | ✅ | ✅ | ✅ | 1.00 | 给它喂食，因为狗饿了，在家里，现在。 |
| EN_L2_01 | 2 | en | ✅ | ✅ | ✅ | 1.00 | turn off all the lights, since the meeting has concluded, in |
| EN_L2_02 | 2 | en | ✅ | ✅ | ✅ | 1.00 | contact maintenance, because the coffee machine is broken, t |
| EN_L2_03 | 2 | en | ✅ | ✅ | ✅ | 1.00 | dispatch security, because the guest complained about noise, |
| ZH_L2_01 | 2 | zh | ✅ | ✅ | ✅ | 1.00 | 关掉所有灯，因为会议已经结束，在5楼大会议室，今天下午6点。 |
| ZH_L2_02 | 2 | zh | ✅ | ✅ | ✅ | 0.00 | 联系维修工，因为咖啡机坏了，到3楼茶水间，明天早上。 |
| ZH_L2_03 | 2 | zh | ✅ | ✅ | ✅ | 1.00 | 派保安上去，因为客人投诉吵闹，在502号套房，今晚11点。 |
| EN_L3_01 | 3 | en | ✅ | ✅ | ✅ | 1.00 | we shut down all backup nodes, to prevent hardware damage an |
| EN_L3_02 | 3 | en | ✅ | ✅ | ✅ | 0.00 | notify the on-call physician, to be safe, in the hospital, w |
| EN_L3_03 | 3 | en | ✅ | ✅ | ✅ | 1.00 | Open the backup registers, because Black Friday traffic is o |
| ZH_L3_01 | 3 | zh | ✅ | ✅ | ✅ | 1.00 | 我们关闭所有备份节点，为了防止硬件损坏和数据丢失，在东翼服务器机房，14:15。 |
| ZH_L3_02 | 3 | zh | ✅ | ✅ | ✅ | 1.00 | 通知值班医生，为了安全起见，在病房，一小时内。 |
| ZH_L3_03 | 3 | zh | ✅ | ✅ | ✅ | 0.00 | 打开所有备用收银台，因为黑五客流过大，在二楼，下午3点前。 |
| EN_L4_01 | 4 | en | ✅ | ✅ | ✅ | 1.00 | I organize all the evidence myself, because calling the poli |
| EN_L4_02 | 4 | en | ✅ | ✅ | ✅ | 1.00 | We go to the Italian restaurant, because my friend recommend |
| EN_L4_03 | 4 | en | ✅ | ✅ | ✅ | 1.00 | I take the bullet train, to save time, to Kyoto, on Friday m |
| ZH_L4_01 | 4 | zh | ✅ | ✅ | ✅ | 1.00 | 我决定自己整理所有证据，因为报警和索赔太麻烦，在家里，今晚。 |
| ZH_L4_02 | 4 | zh | ✅ | ✅ | ✅ | 1.00 | 去意大利餐厅，因为朋友推荐，在第五大道，今晚7点。 |
| ZH_L4_03 | 4 | zh | ✅ | ✅ | ✅ | 1.00 | 坐新干线，因为想去京都旅行，在京都，周五早上。 |

### DX by level (vs Part II baselines)

| Level | N | SC% | SR% | IV% | DX (transformer) | L3 ctrl baseline | L3 human ceiling |
| :-- | :- | :-- | :-- | :-- | :-- | :-- | :-- |
| L1 | 6 | 100% | 100% | 100% | **100%** | 96% (sat.) | — |
| L2 | 6 | 100% | 100% | 100% | **83%** | 96% (sat.) | — |
| L3 | 6 | 100% | 100% | 100% | **67%** | 65% | 100% |
| L4 | 6 | 100% | 100% | 100% | **100%** | 96% (sat.) | — |

**Overall DX:** 88%  (SC 100%, SR 100%, IV 100%)

