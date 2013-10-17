<?php

/**
 * @file
 */

/**
 * Define plugin
 */
$plugin = array(
  'single' => TRUE,
  'title' => t('Example Content Type Plugin'),
  'description' => t('Description'),
  'category' => 'Custom',
  'render callback' => 'mymodule_render',
  'admin info' => 'mymodule_admin_info',
  'defaults' => array(),
);

/**
 * 'admin info' callback for panel pane.
 */
function mymodule_admin_info($subtype, $conf, $contexts) {
  if (!empty($conf)) {
    $block = new stdClass;
    $block->title = $conf['override_title'] ? $conf['override_title_text'] : '';
    $block->content = t('Content');
    return $block;
  }
}

/**
 * Pane rendering callback
 */
function mymodule_render($subtype, $conf, $panel_args, $context = NULL) {
  global $base_url;
  $block = new stdClass();

  // initial content is blank
  $block->title = '';
  $block->content = '';

  // Theme content - return either a render'd drupal_render or a theme()'d tpl

  $block->content = drupal_render($render);
  return $block;
}
