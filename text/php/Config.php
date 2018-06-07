<?php

namespace Config;

// General
const HOST = 'localhost';
const PORT = 4223;

// Bricklet
const UID_LED_STRIP_BRICKLET = 'Fjy';

// Set this to True if LEDStripV2 Bricklet is used
const IS_LED_STRIP_V2 = TRUE;

// Size of LED Pixel matrix
const LED_ROWS = 20;
const LED_COLS = 10;

// Position of R, G and B pixel on LED Pixel
const R_INDEX = 0;
const G_INDEX = 1;
const B_INDEX = 2;

// Text Parameters
const TEXT_FRAME_RATE = 25; // in Hz, valid range: 10 - 100
const TEXT_COLOR_R = NULL; const TEXT_COLOR_G = NULL; const TEXT_COLOR_B = NULL; // = rainbow
//const TEXT_COLOR_R = 255; const TEXT_COLOR_G = 0; const TEXT_COLOR_B = 0; // = red
const TEXT_TOP_OFFSET = 1;

?>
