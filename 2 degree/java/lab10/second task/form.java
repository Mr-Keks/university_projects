package com.company;
import org.jfree.chart.ChartFactory;
import org.jfree.chart.ChartPanel;
import org.jfree.chart.JFreeChart;
import org.jfree.chart.plot.PlotOrientation;
import org.jfree.data.category.DefaultCategoryDataset;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
import java.util.ArrayList;

class PhisicFrame extends JFrame{
   private JButton calc = new JButton("Calculate");
   private JTextField value_volume = new JTextField("", 5);
   private JLabel name_volume = new JLabel("Volume: ");
   private JTextField value_MaxHeight = new JTextField("", 5);
   private JLabel name_MaxHeight = new JLabel("Dam max height: ");
   private JTextField value_MinHeight = new JTextField("", 5);
   private JLabel name_MinHeight = new JLabel("Dam min height: ");
   private JTextField value_step = new JTextField("", 5);
   private JLabel name_step = new JLabel("height step: ");
   private JTextField value_density = new JTextField("", 5);
   private JLabel name_density = new JLabel("Density: ");
   private JLabel empty = new JLabel("");
   private JRadioButton r1 = new JRadioButton("Table");
   private JRadioButton r2 = new JRadioButton("Diagram");

   public PhisicFrame(){
       super("Calculating potential energy");
       this.setBounds(100, 100, 250, 250);
       this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

       Container container = this.getContentPane();
       container.setLayout(new GridLayout(7, 2, 2, 2));
       container.add(name_volume);
       container.add(value_volume);
       container.add(name_MaxHeight);
       container.add(value_MaxHeight);
       container.add(name_MinHeight);
       container.add(value_MinHeight);
       container.add(name_step);
       container.add(value_step);
       container.add(name_density);
       container.add(value_density);

       ButtonGroup group = new ButtonGroup();
       group.add(r1);
       group.add(r2);
       container.add(r1);
       r1.setSelected(true);
       container.add(r2);

       container.add(empty);
       calc.addActionListener(new ButtonEventListener());
       container.add(calc);
   }

   public double getVolume(){
       return Float.parseFloat(this.value_volume.getText());
   }

   public double getMaxHeigh(){
       return Float.parseFloat(this.value_MaxHeight.getText());
   }

   public double getMinHeigh(){
       return Float.parseFloat(this.value_MinHeight.getText());
   }

   public double getStep(){
       return Float.parseFloat(this.value_step.getText());
   }

   public double getDensity(){
       return Float.parseFloat(this.value_density.getText());
   }
   public JTable createTable(){

       ArrayList<String> w = new ArrayList<>();
       ArrayList<String> h = new ArrayList<>();
       String[] nameColumn = new String[]{"№", "W", "h"};

       double i = getMinHeigh();

       for(; i <= getMaxHeigh(); i+=getStep()){
           w.add(String.format("%.2f", getDensity()*getVolume()*9.8*i));
           h.add(String.valueOf(i));
       }

       String[][] tab = new String[w.size()][3];

       for(int z = 0; z < w.size(); z++){
           for(int j = 0; j < 1; j++){
               tab[z][j] = String.valueOf(z+1);
               tab[z][j+1] = w.get(z);
               tab[z][j+2] = h.get(z);
           }
       }

       JTable table = new JTable(tab, nameColumn);
       return table;
   }

   public JFreeChart createDiagram(){
       double i = getMinHeigh();
       double res;
       DefaultCategoryDataset ds = new DefaultCategoryDataset();
       for(; i <= getMaxHeigh(); i+=getStep()){
           res = getDensity()*getVolume()*9.8*i;
           ds.addValue(res, "w", String.format("%.2f",res));
       }
       JFreeChart lc = ChartFactory.createLineChart("ZAl", "h", "w", ds, PlotOrientation.VERTICAL, true, true, false);
       return lc;
   }

   class ButtonEventListener implements ActionListener{
       public void actionPerformed(ActionEvent e){
           if(r1.isSelected()){
               JOptionPane.showMessageDialog(null, new JScrollPane(createTable()), "Output", JOptionPane.PLAIN_MESSAGE);
           }
           else{
               JOptionPane.showMessageDialog(null, new ChartPanel(createDiagram()), "Output", JOptionPane.PLAIN_MESSAGE);
           }

       }
   }
}
