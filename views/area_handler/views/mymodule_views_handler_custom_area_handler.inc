<?php
/**
 * @file
 * Description
 */

class mymodule_views_handler_custom_area_handler extends views_handler_area {
  public function option_definition() {
    $options = parent::option_definition();
    return $options;
  }

  function options_form(&$form, &$form_state) {
    parent::options_form($form, $form_state);

    return $form;
  }

  public function render($empty = FALSE) {
    if (!$empty) {
      // Return a tpl or a drupal_render'd array
      return theme('mymodule_custom_area_handler_display');
    }
    return '';
  }
}
