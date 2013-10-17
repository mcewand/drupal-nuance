<?php
/**
 * Implements hook_views_data_alter
 */
function mymodule_views_data_alter(&$data) {
  $data['databasics']['table']['group']  = t('MyModule');
  $data['views']['mymodule_name_of_area_handler'] = array(
    'title' => t('Global Area Handler'),
    'group' => 'MyModule',
    'help' => t('Area handler.'),
    'area' => array(
      'handler' => 'mymodule_views_handler_custom_area_handler',
    ),
  );
}
