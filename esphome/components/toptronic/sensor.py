# https://github.com/esphome/esphome/blob/dev/esphome/components/fs3000/sensor.py
# https://github.com/esphome/esphome/blob/dev/esphome/components/daly_bms/sensor.py
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import (
    CONF_TYPE
)
from . import (
    toptronic, 
    CONF_TT_ID, 
    TopTronicComponent,

    CONFIG_SCHEMA_BASE,
    CONF_DEVICE_TYPE,
    CONF_DEVICE_ADDR,
    CONF_FUNCTION_GROUP,
    CONF_FUNCTION_NUMBER,
    CONF_DATAPOINT,
)

TopTronicSensor = toptronic.class_(
    "TopTronicSensor", sensor.Sensor
)

TT_TYPE = toptronic.enum("TypeName")
TT_TYPE_OPTIONS = {
    "U8": TT_TYPE.U8,
    "U16": TT_TYPE.U16,
    "U32": TT_TYPE.U32,
    "S8": TT_TYPE.S8,
    "S16": TT_TYPE.S16,
    "S32": TT_TYPE.S32,
    "S64": TT_TYPE.S64,
}

CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(CONF_TT_ID): cv.use_id(TopTronicComponent),
    cv.Required(CONF_TYPE): cv.enum(TT_TYPE_OPTIONS),
}).extend(sensor.sensor_schema(
    TopTronicSensor
)).extend(CONFIG_SCHEMA_BASE)

async def to_code(config):
    tt = await cg.get_variable(config[CONF_TT_ID])
    sens = await sensor.new_sensor(config)
   
    cg.add(sens.set_device_type(config[CONF_DEVICE_TYPE]))
    cg.add(sens.set_device_addr(config[CONF_DEVICE_ADDR]))
    cg.add(sens.set_function_group(config[CONF_FUNCTION_GROUP]))
    cg.add(sens.set_function_number(config[CONF_FUNCTION_NUMBER]))
    cg.add(sens.set_datapoint(config[CONF_DATAPOINT]))
    cg.add(sens.set_type(config[CONF_TYPE]))
    
    cg.add(tt.add_sensor(sens))