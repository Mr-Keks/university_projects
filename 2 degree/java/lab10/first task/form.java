package com.company;
import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

class PhisicFrame extends JFrame{
    private JButton calc = new JButton("Calculate");
    private JTextField value_volume = new JTextField("", 5);
    private JLabel name_volume = new JLabel("Volume: ");
    private JTextField value_height = new JTextField("", 5);
    private JLabel name_height = new JLabel("Dam height: ");
    private JTextField value_density = new JTextField("", 5);
    private JLabel empty = new JLabel("");
    private JLabel name_density = new JLabel("Density: ");

    public PhisicFrame(){
        super("Calculating potential energy");
        this.setBounds(100, 100, 250, 250);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        Container container = this.getContentPane();
        container.setLayout(new GridLayout(4, 2, 2, 2));
        container.add(name_volume);
        container.add(value_volume);
        container.add(name_height);
        container.add(value_height);
        container.add(name_density);
        container.add(value_density);
        container.add(empty);
        calc.addActionListener(new ButtonEventListener());
        container.add(calc);
    }

    public double getVolume(){
        return Float.parseFloat(this.value_volume.getText());
    }

    public double getHeigh(){
        return Float.parseFloat(this.value_height.getText());
    }

    public double getDensity(){
        return Float.parseFloat(this.value_density.getText());
    }
    class ButtonEventListener implements ActionListener{
        public void actionPerformed(ActionEvent e){
            String result = "W = ";
            result += String.valueOf(getVolume()*getVolume()*9.8*getHeigh());
            JOptionPane.showMessageDialog(null, result, "Output", JOptionPane.PLAIN_MESSAGE);
        }
    }
}